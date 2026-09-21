"""Twelve packet fixtures. Structural fixtures execute the real inventory.
Semantic fixtures test reviewer-annotated distinctions, not automatic reasoning.
"""
from pathlib import Path
import json,os,subprocess,sys,tempfile
from triage import available,issues,cycles
OUT=Path(__file__).resolve().parents[1]
results=[]
def check(name,value):
 assert value,name
 results.append({'fixture':name,'passed':True})
def s(cap='C',order=1,**kw):return dict(capability=cap,order=order,sufficient=True,**kw)
def u(cap='C',order=2,**kw):return dict(id='use',capability=cap,order=order,**kw)
check('01 genuinely defined before required use',available(u(),[s()]))
check('02 concrete example sufficient before formal definition',available(u(),[s(kind='example'),s(order=3,kind='definition')]))
check('03 exercise before first usable rule',issues([u(order=1)],[s(order=2)])==['use'])
check('04 unused optional preview',issues([u(optional=True)],[])==[])
check('05 required assessment depends only on optional preview',issues([u()],[s(optional=True)])==['use'])
check('06 supplied theorem before independent later proof',available(u(),[s(kind='supplied_theorem')]) and not cycles([('theorem','entry_lemma')]))
check('07 deferred proof cycle',bool(cycles([('A','B'),('B','C'),('C','A')])))
check('08 coordinate three-form is not arbitrary triple wedge',not available(u(cap='arbitrary_triple'),[s(cap='coordinate_three')]))
check('09 macro declaration is not visible teaching',not available(u(),[s(visible=False,kind='macro')]))
check('10 mathematical graphic label creates a visible use',issues([u(kind='graphic_label')],[])==['use'])
with tempfile.TemporaryDirectory(prefix='mvc-audit-fixture-') as tmp:
 root=Path(tmp);src=root/'source';src.mkdir();out=root/'out';(out/'section-text').mkdir(parents=True)
 (src/'main.ptx').write_text('<book xmlns:xi="http://www.w3.org/2001/XInclude"><chapter xml:id="c"><title>C</title><xi:include href="z.xml"/><xi:include href="a.xml"/></chapter></book>')
 for filename,key in [('z.xml','first'),('a.xml','second')]:
  (src/filename).write_text(f'<section xml:id="{key}"><title>{key}</title><p>Visible text.</p></section>')
 env=dict(os.environ,MVC_AUDIT_ROOT=str(root),MVC_AUDIT_OUTPUT=str(out),MVC_AUDIT_SNAPSHOT='fixture')
 def run():
  r=subprocess.run([sys.executable,str(Path(__file__).with_name('inventory.py'))],env=env,capture_output=True,text=True)
  assert r.returncode==0,r.stderr
  return json.loads((out/'inventory.json').read_text(encoding='utf-8'))
 inv=run();check('11 XInclude order overrides alphabetical filenames',[x['id'] for x in inv['sections']]==['first','second'])
 (src/'a.xml').unlink();inv=run();check('12 missing fragment makes coverage explicitly incomplete',any(x['type']=='parse_or_missing' for x in inv['issues']) and len(inv['sections'])==1)
(OUT/'evidence/fixtures.json').write_text(json.dumps({'scope':'10 reviewer-annotation tests;2 production-inventory tests. Passing is not semantic certification.','results':results},indent=2),encoding='utf-8')
print('PASS',len(results),'fixtures')
