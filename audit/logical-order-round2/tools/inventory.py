"""Snapshot inventory, source extraction and candidate enumeration; not a logical verifier."""
from pathlib import Path
from lxml import etree as E
from xml.parsers import expat
from collections import Counter
import hashlib,json,re,subprocess,os
ROOT=Path(os.environ.get('MVC_AUDIT_ROOT',Path(__file__).resolve().parents[3])); OUT=Path(os.environ.get('MVC_AUDIT_OUTPUT',ROOT/'audit/logical-order-round2'))
ID='{http://www.w3.org/XML/1998/namespace}id';XI='{http://www.w3.org/2001/XInclude}include'
SHA=os.environ.get('MVC_AUDIT_SNAPSHOT') or subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
records=[];files=[];sections=[];ids={};refs=[];issues=[];tasks=[];file_occ=Counter();serial=0
roles={'title','p','m','md','mdn','mrow','li','cell','caption','shortdescription','description','theorem','lemma','corollary','proposition','proof','definition','example','exercise','task','project','problem','activity','investigation','exploration','question','hint','solution','asymptote','latex-image','program'}
formal={'exercise','project','problem','activity','investigation','exploration','question','task'}
def text(e):return ' '.join(''.join(e.itertext()).split())
def parse(path):
 raw=path.read_bytes();positions=[];stack=[];parser=expat.ParserCreate()
 def start(name,attrs):
  rec=[parser.CurrentLineNumber,None];positions.append(rec);stack.append(rec)
 def end(name):stack.pop()[1]=parser.CurrentLineNumber
 parser.StartElementHandler=start;parser.EndElementHandler=end;parser.Parse(raw,True)
 tree=E.fromstring(raw);nodes=[n for n in tree.iter() if isinstance(n.tag,str)]
 assert len(nodes)==len(positions),(path,len(nodes),len(positions))
 return raw,tree,dict(zip(nodes,positions))
def visit(path,chain=(),chapter=None,section=None):
 global serial
 path=path.resolve();rel=path.relative_to(ROOT).as_posix()
 if rel in chain:issues.append({'type':'include_cycle','path':rel});return
 try:raw,tree,positions=parse(path)
 except Exception as error:issues.append({'type':'parse_or_missing','path':rel,'error':str(error)});return
 file_occ[rel]+=1;occ=file_occ[rel];digest=hashlib.sha256(raw).hexdigest(); ancestry=[*chain,rel]
 files.append({'path':rel,'sha256':digest,'snapshot':SHA,'occurrence':occ,'ancestry':ancestry,'lines':len(raw.splitlines())})
 local_lines=[]
 def walk(e,chapter,section):
  global serial
  if not isinstance(e.tag,str):return
  if e.tag==XI:
   if e.get('xpointer') or e.get('parse','xml')!='xml':issues.append({'type':'unsupported_include','path':rel,'line':e.sourceline,'attrs':dict(e.attrib)});return
   visit(path.parent/e.get('href'),tuple(ancestry),chapter,section);return
  ident=e.get(ID); serial+=1; node_id=f'n{serial:06d}'; start,end=positions[e]
  if e.tag in ('chapter','appendix'):chapter={'id':ident,'title':text(e.find('title')),'kind':e.tag}
  if e.tag=='section':
   section={'order':len(sections)+1,'id':ident,'title':text(e.find('title')),'path':rel,'sha256':digest,'lines':[start,end],'chapter':chapter,'occurrence':occ,'ancestry':ancestry};sections.append(section)
  ancestor_tags=[a.tag for a in e.iterancestors() if isinstance(a.tag,str)];ancestor_ids=[a.get(ID) for a in e.iterancestors() if a.get(ID)]
  containers=[e,*e.iterancestors()]
  optional=[]
  for a in containers:
   if not isinstance(a.tag,str):continue
   title=a.find('title')
   if title is not None and re.search(r'optional|preview|looking ahead|gateway',text(title),re.I):optional.append({'id':a.get(ID),'title':text(title)})
  role='hint' if 'hint' in [e.tag,*ancestor_tags] else 'solution' if 'solution' in [e.tag,*ancestor_tags] else 'preview_or_optional_candidate' if optional else 'default_required'
  loc={'snapshot':SHA,'path':rel,'sha256':digest,'lines':[start,end],'xml_id':ident,'nearest_id':ident or (ancestor_ids[0] if ancestor_ids else None),'xpath':e.getroottree().getpath(e),'occurrence':occ,'ancestry':ancestry,'node_id':node_id,'order':serial,'section_id':section['id'] if section else None,'section_order':section['order'] if section else None,'chapter':chapter,'role':e.tag,'student_status':role,'optional_markers':optional}
  if ident:
   if ident in ids:issues.append({'type':'duplicate_id','xml_id':ident,'first':ids[ident]['node_id'],'second':node_id})
   ids[ident]=loc.copy()
  if e.tag in roles:
   loc['text']=text(e); loc['xrefs']=[dict(x.attrib) for x in e.iter('xref')];records.append(loc)
  if e.tag=='xref':
   for attr in ['ref','first','last']:
    for ref in re.split(r'[,\s]+',e.get(attr,'').strip()):
     if ref:refs.append({'from':node_id,'source':loc,'target_id':ref,'attribute':attr})
  if e.tag in formal:
   tasks.append({**loc,'task_key':ident or f'{rel}:{start}:{occ}','kind':'formal','text':text(e),'status':'requires_semantic_classification'})
  elif e.tag in ('subsection','paragraphs') and e.find('title') is not None and re.search(r'project|problems|exercises|practice|review',text(e.find('title')),re.I) and not any(t in formal for t in ancestor_tags):
   tasks.append({**loc,'task_key':ident or f'{rel}:{start}:{occ}','kind':'assessment_bundle_candidate','text':text(e),'status':'requires_semantic_classification'})
  elif e.tag=='p' and not any(t in formal|{'example','proof','hint','solution','theorem','definition'} for t in ancestor_tags) and re.search(r'^(?:\d+[.)]\s*)?(?:Find|Compute|Show|Explain|Verify|Sketch|Describe|Choose|Compare|Determine|Prove|Calculate|Investigate|Build|Write|Explore|Check)\b',text(e)):
   tasks.append({**loc,'task_key':f'{rel}:{start}:{occ}','kind':'directive_candidate','text':text(e),'status':'requires_semantic_classification'})
  # Atomic reading extraction includes every text/math in paragraphs, and raw graphic/code bodies.
  if e.tag in ('title','p','caption','shortdescription','description','latex-image','asymptote','program','cell','md','mdn','me','men','li') and not any(t in ('p','caption','shortdescription','description','latex-image','asymptote','program','cell','md','mdn','me','men','li') for t in ancestor_tags):
   local_lines.append(f'[{start}-{end} {e.tag} {ident or (ancestor_ids[0] if ancestor_ids else "")} {role}]\n'+''.join(e.itertext()).strip()+'\n')
  for child in e:walk(child,chapter,section)
 walk(tree,chapter,section)
 if tree.tag=='section':(OUT/'section-text'/f'{tree.get(ID)}.txt').write_text('\n'.join(local_lines),encoding='utf-8')
visit(ROOT/'source/main.ptx')
for ref in refs:
 if ref['target_id'] not in ids:issues.append({'type':'unresolved_xref','target_id':ref['target_id'],'source':ref['source']})
active={f['path'] for f in files};all_sources={p.relative_to(ROOT).as_posix() for p in (ROOT/'source').rglob('*') if p.suffix in ('.xml','.ptx')}
meta={'schema_version':1,'snapshot':SHA,'branch':'fixture' if os.environ.get('MVC_AUDIT_SNAPSHOT') else subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip(),'git_status_at_inventory':'' if os.environ.get('MVC_AUDIT_SNAPSHOT') else subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True),'source_tree_hash':hashlib.sha256('\n'.join(f['path']+' '+f['sha256'] for f in files).encode()).hexdigest(),'files':files,'sections':sections,'inactive_sources':sorted(all_sources-active),'issues':issues,'scope_note':'An inventory and candidate list, not a claim of semantic review or dependency verification.'}
for name,obj in [('inventory.json',meta),('nodes.json',records),('id-index.json',ids),('cross-references.json',refs),('task-inventory.json',tasks)]: (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
print('FILES',len(files),'SECTIONS',len(sections),'CHAPTER_SECTIONS',sum(s['chapter']['kind']=='chapter' for s in sections),'APPENDIX_SECTIONS',sum(s['chapter']['kind']=='appendix' for s in sections),'IDS',len(ids),'XREFS',len(refs),'ISSUES',len(issues))
print('TASK CANDIDATES',dict(Counter(t['kind'] for t in tasks)))
print('SECTIONS BY CHAPTER',dict(Counter(s['chapter']['id'] for s in sections)))

