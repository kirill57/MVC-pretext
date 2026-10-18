"""Inspect every active PreTeXt page in a real Chromium browser.

Screenshots and diagnostics stay in the requested evidence directory. This is
layout/link evidence, not a mathematical proof checker. Run live and locally.
"""
import argparse
import asyncio
import json
import re
from pathlib import Path
from urllib.parse import urljoin

from lxml import etree as E
from PIL import Image, ImageDraw
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
ID = '{http://www.w3.org/XML/1998/namespace}id'

METRICS = r"""() => {
  const main = document.querySelector('main') || document.body;
  const rect = main.getBoundingClientRect();
  const visible = e => !!(e.getClientRects().length && getComputedStyle(e).visibility !== 'hidden');
  const describe = e => ({tag:e.tagName,id:e.id,text:e.textContent.trim().slice(0,500),
    width:Math.round(e.getBoundingClientRect().width),scroll:e.scrollWidth,client:e.clientWidth});
  const allMath = [...main.querySelectorAll('mjx-container')];
  return {
    title:document.title, heading:main.querySelector('h1,h2')?.innerText,
    bodyWidth:document.body.scrollWidth, viewport:innerWidth, mainWidth:Math.round(rect.width),
    mathCount:allMath.length,
    mathErrors:[...main.querySelectorAll('mjx-merror,merror,.mjx-merror')].map(describe),
    images:[...main.querySelectorAll('img')].map(e=>({src:e.currentSrc||e.src,alt:e.alt,
      complete:e.complete,width:e.naturalWidth,visible:visible(e)})),
    overflow:[...main.querySelectorAll('.displaymath,table,figure')].filter(visible).filter(e=>{
      const r=e.getBoundingClientRect();
      return e.scrollWidth>e.clientWidth+5 || r.right>rect.right+6 || r.width>rect.width+6;
    }).map(describe),
    textProblems:(main.innerText.match(/Placeholder[^\n]*|TODO[^\n]*|TBD[^\n]*|\uFFFD/g)||[]),
    links:[...main.querySelectorAll('a[href]')].map(e=>e.getAttribute('href')),
    ids:[...document.querySelectorAll('[id]')].map(e=>e.id)
  };
}"""


def inventory():
    doc = E.parse(str(ROOT / 'source/main.ptx'))
    doc.xinclude()
    root = doc.getroot()
    pages = []
    for n in root.iter():
        if n.tag in ('book','part','chapter','appendix','section','preface','backmatter') and n.get(ID):
            title = n.find('title')
            pages.append({'id': n.get(ID), 'kind': n.tag,
                          'title': ''.join(title.itertext()) if title is not None else n.get(ID),
                          'source': str(n.base), 'line': n.sourceline})
    ids = [n.get(ID) for n in root.iter() if n.get(ID)]
    references = [(n.get(a), n.base, n.sourceline) for n in root.iter('xref')
                  for a in ('ref','first','last') if n.get(a)]
    unresolved = [(ref, path, line) for refs,path,line in references
                  for ref in re.split(r'[,\s]+', refs) if ref and ref not in ids]
    return pages, {'counts': {k: len(root.findall('.//' + k)) for k in
                   ('chapter','appendix','section','subsection','p','image','figure','exercise','theorem')},
                   'id_count':len(ids), 'duplicates':sorted({x for x in ids if ids.count(x)>1}),
                   'unresolved':unresolved}


def contact_sheets(items, output, prefix):
    cols, rows, w, h = 4, 3, 360, 300
    for start in range(0, len(items), cols*rows):
        sheet = Image.new('RGB',(cols*w,rows*h),'#e5e7eb')
        draw = ImageDraw.Draw(sheet)
        for i, item in enumerate(items[start:start+cols*rows]):
            x,y = (i%cols)*w,(i//cols)*h
            image = Image.open(output/item['file']).convert('RGB')
            image.thumbnail((w-12,h-45))
            sheet.paste(image,(x+(w-image.width)//2,y+42))
            draw.text((x+5,y+5),f"{start+i+1}: {item['page'][:40]}",fill='black')
            draw.text((x+5,y+21),item.get('id','')[:45],fill='black')
        sheet.save(output/f'{prefix}-{start//(cols*rows)+1:02}.jpg',quality=88)


async def run(args):
    output = Path(args.output).resolve()
    output.mkdir(parents=True,exist_ok=True)
    pages,structure = inventory()
    (output/'structure.json').write_text(json.dumps(structure,indent=2),encoding='utf-8')
    results,figures,tables,headers = [],[],[],[]
    queue = asyncio.Queue()
    for i, record in enumerate(pages):
        if args.limit and i>=args.limit: break
        if args.page and record['id'] not in args.page: continue
        queue.put_nowait((i,record))
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width':1280,'height':960},device_scale_factor=1)
        async def worker():
            page = await context.new_page()
            while not queue.empty():
                index,record = await queue.get()
                ident = record['id']
                errors = []
                on_error = lambda err: errors.append(str(err))
                page.on('pageerror',on_error)
                try:
                    response = await page.goto(urljoin(args.base.rstrip('/')+'/',ident+'.html'),
                                               wait_until='load',timeout=60000)
                    await page.evaluate("async()=>{if(window.MathJax?.startup?.promise) await window.MathJax.startup.promise;await document.fonts.ready;}")
                    await page.wait_for_timeout(180)
                    folds = await page.locator('details').evaluate_all("els=>els.map(e=>({id:e.id,title:e.querySelector('summary')?.innerText,open:e.open}))")
                    await page.locator('details').evaluate_all("els=>els.forEach(e=>e.open=true)")
                    await page.evaluate("async()=>{if(window.MathJax?.startup?.promise) await window.MathJax.startup.promise;}")
                    metrics = await page.evaluate(METRICS)
                    result = {**record,'url':page.url,'status':response.status if response else None,
                              'folds':folds,'pageErrors':errors,**metrics}
                    main = page.locator('main').first
                    box = await main.bounding_box()
                    if box:
                        header = f'page-{index:03}-{ident}.png'
                        await page.screenshot(path=str(output/header),clip={'x':max(0,box['x']),
                          'y':max(0,box['y']),'width':min(box['width'],1280-box['x']),
                          'height':min(box['height'],850)})
                        headers.append({'page':ident,'id':record['title'],'file':header,'order':index})
                    if args.screenshots:
                        # Sticky navigation can otherwise obscure the top of an
                        # element screenshot after Playwright scrolls to it.
                        await page.evaluate("""()=>{for(const e of document.querySelectorAll('body *')) {
                          if(e.closest('main') || e.contains(document.querySelector('main'))) continue;
                          if(['fixed','sticky'].includes(getComputedStyle(e).position)) {
                            e.dataset.auditVisibility=e.style.visibility;
                            e.style.visibility='hidden';
                          }
                        }}""")
                        for category,selector,items in [('figure','main figure',figures),('table','main table',tables)]:
                            locs=page.locator(selector)
                            for j in range(await locs.count()):
                                element=locs.nth(j)
                                if not await element.is_visible(): continue
                                eid=await element.get_attribute('id') or f'{category}-{j}'
                                filename=f'{category}-{index:03}-{j:02}.png'
                                try:
                                    target=element
                                    box=await target.bounding_box()
                                    if not box or box['width']==0 or box['height']==0:
                                        # Side-by-side child figures use display:contents;
                                        # their image box is the screenshot surface.
                                        target=element.locator('.image-box').first
                                    await target.scroll_into_view_if_needed()
                                    for frame in await element.locator('iframe.asymptote').all():
                                        await page.wait_for_function("""e=>e.contentDocument?.readyState==='complete'
                                          && !!e.contentDocument.querySelector('canvas,svg')""",
                                          arg=await frame.element_handle(), timeout=15000)
                                        await page.wait_for_timeout(300)
                                    await target.screenshot(path=str(output/filename),timeout=12000)
                                    items.append({'page':ident,'id':eid,'file':filename,'order':index*100+j})
                                except Exception as exc:
                                    result.setdefault('screenshotErrors',[]).append(f'{eid}: {exc}')
                        await page.evaluate("""()=>document.querySelectorAll('[data-audit-visibility]').forEach(e=>{
                          e.style.visibility=e.dataset.auditVisibility;delete e.dataset.auditVisibility;
                        })""")
                    if args.mobile:
                        await page.set_viewport_size({'width':390,'height':844})
                        await page.wait_for_timeout(60)
                        result['mobile']=await page.evaluate(METRICS)
                        await page.set_viewport_size({'width':1280,'height':960})
                    results.append(result)
                except Exception as exc:
                    results.append({**record,'error':str(exc)})
                page.remove_listener('pageerror',on_error)
                queue.task_done()
                if len(results)%10==0: print(f'Inspected {len(results)}/{len(pages)} pages',flush=True)
                (output/'pages.json').write_text(json.dumps(sorted(results,key=lambda x:x['id']),indent=2),encoding='utf-8')
            await page.close()
        await asyncio.gather(*(worker() for _ in range(args.workers)))
        await browser.close()
    for items,name in ((figures,'figures'),(tables,'tables'),(headers,'pages')):
        items.sort(key=lambda x:x['order'])
        (output/f'{name}-screenshots.json').write_text(json.dumps(items,indent=2),encoding='utf-8')
        contact_sheets(items,output,name)
    summary = {'pages':len(results),'failed_pages':[r['id'] for r in results if r.get('error') or r.get('status')!=200],
       'page_errors':[{'page':r['id'],'errors':r['pageErrors']} for r in results if r.get('pageErrors')],
       'math_errors':[{k:r[k] for k in ('id','mathErrors')} for r in results if r.get('mathErrors')],
       'missing_images':[{'page':r['id'],'images':[x for x in r.get('images',[]) if x['width']==0]} for r in results if any(x['width']==0 for x in r.get('images',[]))],
       'overflow':[{k:r[k] for k in ('id','overflow')} for r in results if r.get('overflow')],
       'placeholders':[{'page':r['id'],'text':r['textProblems']} for r in results if r.get('textProblems')],
       'mobile_page_overflow':[{'page':r['id'],'width':r['mobile']['bodyWidth']} for r in results
                               if r.get('mobile',{}).get('bodyWidth',0)>r.get('mobile',{}).get('viewport',0)+5],
       'optional_open':[{'page':r['id'],'folds':[f for f in r.get('folds',[])
                         if f.get('open') and 'Optional' in (f.get('title') or '')]} for r in results
                         if any(f.get('open') and 'Optional' in (f.get('title') or '') for f in r.get('folds',[]))],
       'screenshot_errors':[{'page':r['id'],'errors':r['screenshotErrors']} for r in results if r.get('screenshotErrors')],
       'screenshots':{'figures':len(figures),'tables':len(tables),'pages':len(headers)}}
    (output/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps({k:v if not isinstance(v,list) else len(v) for k,v in summary.items()},indent=2),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--workers',type=int,default=3)
    parser.add_argument('--limit',type=int)
    parser.add_argument('--page',action='append',help='Inspect only these page IDs; may be repeated.')
    parser.add_argument('--screenshots',action='store_true')
    parser.add_argument('--mobile',action='store_true')
    asyncio.run(run(parser.parse_args()))
