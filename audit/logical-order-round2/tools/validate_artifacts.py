"""Validate provenance, coverage and recorded edges, not mathematical truth."""
from pathlib import Path
from collections import Counter
import json,hashlib,sys
from triage import cycles
P=Path(__file__).resolve().parents[1];ROOT=P.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
inv=read(P/'inventory.json');idx=read(P/'id-index.json');coverage=read(P/'coverage.json');graphs=read(P/'dependency-graphs.json')
files={f['path']:f for f in inv['files']};order={f['path']:i for i,f in enumerate(inv['files'])};errors=[];warnings=[];locations=0;jsoncount=0
def checkloc(d,name):
 global locations
 if d.get('path') in files and 'lines' in d:
  locations+=1; a=d['lines'];n=files[d['path']]['lines']
  valid=a==n if isinstance(a,int) else isinstance(a,list) and len(a)==2 and all(isinstance(x,int) for x in a) and 1<=a[0]<=a[1]<=n
  if not valid:errors.append([name,'bad_lines',d['path'],a,n])
  if d.get('sha256') and d['sha256']!=files[d['path']]['sha256']:errors.append([name,'hash_mismatch',d['path']])
  if d.get('snapshot') and d['snapshot']!=inv['snapshot']:errors.append([name,'snapshot_mismatch',d['path']])
  if d.get('xml_id') and d['xml_id'] not in idx:errors.append([name,'unknown_xml_id',d['xml_id']])
 for v in d.values():
  if isinstance(v,dict):checkloc(v,name)
  elif isinstance(v,list):
   for x in v:
    if isinstance(x,dict):checkloc(x,name)
for p in P.rglob('*.json'):
 if p.name=='artifact-validation.json':continue
 try:d=read(p);jsoncount+=1
 except Exception as e:errors.append([str(p),'json',str(e)]);continue
 if isinstance(d,dict):checkloc(d,p.relative_to(P).as_posix())
 elif isinstance(d,list):
  for x in d:
   if isinstance(x,dict):checkloc(x,p.relative_to(P).as_posix())
for path,f in files.items():
 if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=f['sha256']:errors.append(['source_changed',path])
for t in coverage['task_candidate_reconciliation']:
 if t['status']=='UNRESOLVED':errors.append(['unresolved_candidate',t['inventory_task_key']])
 if t['kind']=='formal' and t['status']!='witnessed':errors.append(['formal_without_witness',t['inventory_task_key']])
future=[];solution=[]
for e in graphs['learning_availability']['edges']:
 a=e['support'];b=e['use']
 if a.get('path') in order and b.get('path') in order and a.get('lines') and b.get('lines'):
  if (order[a['path']],a['lines'][0])>(order[b['path']],b['lines'][0]):
   local=a['path']==b['path'] and a['lines'][1]<=b['lines'][1]
   disposition='local project scaffold inside enclosing task bundle; individual hand-in steps have separate prior-support witnesses' if local else 'explicit navigation gap LO-13; later appendix not credited as earlier teaching' if e['availability']=='navigation_gap' else 'UNRESOLVED'
   future.append({'reviewer':e['reviewer'],'support':a,'use':b,'status':e['availability'],'disposition':disposition})
   if disposition=='UNRESOLVED':errors.append(['unresolved_forward_support',b,a])
 if '/solution' in a.get('xpath',''):solution.append(e)
def ident(x):return x.get('xml_id',x.get('capability_id')) if isinstance(x,dict) else x
pe=[]
for e in graphs['mathematical_proof']['edges']:
 a,b=ident(e['support']),ident(e['result'])
 if a and b and a!=b:pe.append((a,b))
cs=cycles(pe)
if cs:errors.append(['recorded_proof_cycles',cs])
result={'snapshot':inv['snapshot'],'json_files_parsed':jsoncount,'source_location_records_checked':locations,'active_file_hashes_checked':len(files),'formal_task_elements_witnessed':sum(t['kind']=='formal' for t in coverage['task_candidate_reconciliation']),'inventory_candidates_reconciled':len(coverage['task_candidate_reconciliation']),'learning_edges_checked':len(graphs['learning_availability']['edges']),'proof_premise_edges_checked':len(pe),'recorded_proof_cycles':cs,'forward_learning_edges_for_manual_disposition':future,'solution_only_support_edges_for_manual_disposition':solution,'errors':errors,'warnings':warnings,'ceiling':'Mechanical record checks and cycle check on the recorded critical graph, not complete proof certification. Forward/scaffold classifications require manual review.'}
(P/'evidence/artifact-validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
print('JSON',jsoncount,'LOCATIONS',locations,'HASHES',len(files),'ERRORS',len(errors),'FORWARD',len(future),'SOLUTION',len(solution),'PROOF_CYCLES',len(cs))
for e in errors[:12]:print(e)
for e in future[:20]:print('FORWARD',e['reviewer'],e['use'].get('xml_id'),e['use']['lines'],e['support'].get('xml_id'),e['support']['lines'],e['status'])
sys.exit(bool(errors))
