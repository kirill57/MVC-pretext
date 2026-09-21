"""Integrate reviewed fragments without upgrading read-only/partial states."""
from pathlib import Path
import json,hashlib,re
from collections import Counter
P=Path(__file__).resolve().parents[1];ROOT=P.parents[1]
def read(path):return json.loads((P/path).read_text(encoding='utf-8'))
def save(path,data):(P/path).write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
INV=read('inventory.json');I=read('id-index.json');TASKS=read('task-inventory.json');SNAP=INV['snapshot'];F=['foundations','reference','root','greens-surfaces','general-forms']
def ev(key,lines=None):
 d=I['how-to-read' if key=='ENTRY' else key].copy();d.pop('optional_markers',None)
 if lines:d['lines']=list(lines)
 return d
def supplement(obj):
 if isinstance(obj,list):return [supplement(x) for x in obj]
 if not isinstance(obj,dict):return obj
 d={k:supplement(v) for k,v in obj.items()}
 if d.get('path') in filehash:
  d.setdefault('snapshot',SNAP);d.setdefault('sha256',filehash[d['path']])
  if d.get('xml_id') in I and I[d['xml_id']]['path']==d['path']:
   # A reviewer may give a narrower/custom line range on a containing ID.
   # Keep that range, but do not retain a copied child XPath/node identity.
   for k in ('node_id','xpath','section_id','section_order','occurrence'):
    if k in d:d[k]=I[d['xml_id']][k]
 return d
filehash={f['path']:f['sha256'] for f in INV['files']}
sections={};wrappers={};concepts=[];learning=[];proof=[];roots=[];missing=[];tasks=[];dispositions=[];registry={}
for f in F:
 base='fragments/'+f+'/'
 cov=read(base+'coverage.json'); entries=cov if isinstance(cov,list) else cov['sections']
 extra=[] if isinstance(cov,list) else cov.get('wrappers',cov.get('wrappers_and_backmatter',[]))
 for s in entries:
  sid=s.get('section_id',s.get('id'));s={'reviewer':f,**s}
  if sid in {x['id'] for x in INV['sections']}:assert sid not in sections;sections[sid]=s
  else:extra.append(s)
 for w in extra:
  path=w.get('path',w.get('evidence',{}).get('path'))
  if path:wrappers.setdefault(path,[]).append({'reviewer':f,**w})
 con=read(base+'concepts.json');cl=con if isinstance(con,list) else con.get('concepts',con.get('capabilities',[]))
 for c in cl:concepts.append({'reviewer':f,**c})
 g=read(base+'graphs.json');reg=g.get('support_registry',g.get('support_nodes',{}));registry[f]=reg
 le=g.get('learning_edges',[x for x in g.get('edges',[]) if x.get('graph')=='learning'])
 pe=g.get('proof_edges',[x for x in g.get('edges',[]) if x.get('graph')=='proof'])
 learning += [{'reviewer':f,**x} for x in le];proof += [{'reviewer':f,**x} for x in pe]
 roots += [{'reviewer':f,'record':r} for r in g.get('supplied_roots',g.get('roots',[]))]
 missing += [{'reviewer':f,'record':r} for r in g.get('missing_supports',[])]
 td=read(base+'task-witnesses.json')
 if f=='general-forms':
  for row in td['rows']:
   w=td['witnesses'][row['witness']];tasks.append({'reviewer':f,**row,'outline':w['solution_outline'],'support_evidence':[td['support_evidence'][x] for x in w['support_ids']]})
  dispositions += [{'reviewer':f,'task_key':x[0],'disposition':x[1]} for x in td['exclusions']]
 else:
  tl=td if isinstance(td,list) else td.get('tasks',td.get('witnesses',[]))
  for t in tl:
   r={'reviewer':f,**t}
   if f=='foundations':r['support_evidence']=[reg[x] if x in reg else ev(x) for x in t['support_ids']]
   tasks.append(r)
 if f=='foundations':
  dispositions += [{'reviewer':f,**x,'task_key':x['task_id'],'node_id':x['evidence']['node_id']} for x in read(base+'candidate-dispositions.json')]

records=[]
challenge_paths={
'foundations':'fragments/general-forms/challenges-general-v-foundations.md',
'general-forms':'fragments/foundations/challenges-foundations-v-general.md',
'reference':'fragments/root/challenges-root-v-reference.md',
'root':'fragments/reference/independent-challenge-root.md',
'greens-surfaces':'fragments/root/challenges-root-v-greens-surfaces.md'}
for s in INV['sections']:
 r=sections[s['id']];fragment=r['reviewer'];ch=challenge_paths[fragment]
 r={'snapshot':SNAP,**s,**r,'section_id':s['id'],'inventoried':True,'mechanically_scanned':True,'independent_challenge_completed':False,'independent_challenge_scope':'Selected defects and important nonissues in this partition, not a second full-section reading.','partition_challenge_artifact':ch,'partition_challenge_completed':(P/ch).exists()}
 r.setdefault('unresolved',r.get('support_limitations',[]));r.setdefault('task_witnesses_complete',True)
 r['graphics_review']={'source':True,'rendered':False,'scope':'Source labels, captions, descriptions and embedded code read; whole-section rendered inspection not claimed.'}
 if s['id']=='sec-5-derivatives-and-integrals-of-vector-valued-functions':r['graphics_review'].update(rendered=True,scope='Only current-run surface-grid definition/link and cone figure/caption spot-checked in the local browser; other figures remain source-only.')
 records.append(r)
assert len(records)==len(INV['sections'])==len(sections)
wrapper_files=[x for x in INV['files'] if x['path'] not in {s['path'] for s in INV['sections']}]
wrapperrecords=[]
for w in wrapper_files:
 assert w['path'] in wrappers,w['path']
 wrapperrecords.append({**w,'semantic_read':True,'reviews':wrappers[w['path']],'role':'wrapper/frontmatter/backmatter/docinfo; macros are not instruction'})

normalizedtasks=[]
for t in tasks:
 loc=t.get('evidence',t.get('source',{})); path=t.get('path',loc.get('path'));lines=t.get('lines',loc.get('lines')) or [t.get('line'),t.get('line')]
 key=t.get('task_key',t.get('task_id'));xmlid=t.get('xml_id',loc.get('xml_id')) or (key if key in I else None)
 normalizedtasks.append({**t,'task_key':key,'path':path,'lines':lines,'xml_id':xmlid,'node_id':t.get('node_id',loc.get('node_id')),'outline':t.get('outline',t.get('solution_outline'))})
bykey={};bynode={};bypathline={}
for t in normalizedtasks:
 bykey.setdefault(t['task_key'],[]).append(t)
 if t['node_id']:bynode.setdefault(t['node_id'],[]).append(t)
 if t['path'] and t['lines'][0]:bypathline.setdefault((t['path'],t['lines'][0]),[]).append(t)
reconciled=[]
for t in TASKS:
 found=bykey.get(t['task_key'],[]) or bykey.get(t['xml_id'],[]) or bynode.get(t['node_id'],[]) or bypathline.get((t['path'],t['lines'][0]),[])
 ds=[d for d in dispositions if t['node_id'] in [d.get('node_id'),d.get('candidate_id'),d.get('task_key')] or t['task_key'] in [d.get('task_key'),d.get('candidate_id')] or (d.get('path')==t['path'] and d.get('line')==t['lines'][0])]
 reconciled.append({'inventory_task_key':t['task_key'],'node_id':t['node_id'],'path':t['path'],'lines':t['lines'],'kind':t['kind'],'witness_keys':[x['task_key'] for x in found],'dispositions':ds,'status':'witnessed' if found else 'classified_nonassessment' if ds else 'UNRESOLVED'})
bad=[r for r in reconciled if r['status']=='UNRESOLVED'];print('UNRECONCILED',len(bad));print([(x['node_id'],x['kind']) for x in bad])

normalized_learning=[];normalized_proof=[];deferred=[]
def resolve_record(value,reviewer):
 if isinstance(value,str):
  if value in I or value=='ENTRY':return ev(value)
  if value in registry.get(reviewer,{}):return registry[reviewer][value]
  return {'capability_id':value,'availability':'missing or abstract support; see original record'}
 return value
for e in learning:
 support=e.get('support') or e.get('source_evidence') or e.get('from_evidence') or e.get('source')
 use=e.get('use') or e.get('target_evidence') or e.get('to_evidence') or e.get('target')
 support=resolve_record(support,e['reviewer']);use=resolve_record(use,e['reviewer'])
 assert isinstance(support,dict) and isinstance(use,dict),(e['reviewer'],e)
 normalized_learning.append({'reviewer':e['reviewer'],'support':support,'use':use,'capability':e.get('capability',e.get('capability_use',e.get('capability_support_id',e.get('from',e.get('source_id',e.get('source')))))),'availability':e.get('availability',e.get('status',e.get('verdict','see source witness'))),'scope':e.get('scope',e.get('assessment_status','see source witness'))})
for e in proof:
 if e.get('status','').startswith('deferred proof'):
  deferred.append({'from':e['source_evidence'],'destination':e['target_evidence'],'status':'destination independently checked by root and greens-surfaces reader','scope':'C1 regular local surface sheet; full first-order remainder and local graph argument'})
  continue
 result=e.get('result') or e.get('target_evidence') or e.get('to_evidence') or e.get('target')
 supports=e.get('supports') or [e.get('support') or e.get('source_evidence') or e.get('from_evidence') or e.get('source')]
 for support in supports:
  support=resolve_record(support,e['reviewer']);result=resolve_record(result,e['reviewer'])
  normalized_proof.append({'reviewer':e['reviewer'],'support':support,'result':result,'inference':e.get('inference',e.get('reason',e.get('scope'))),'status':e.get('status','reviewed source argument')})
for a,b,status in [
 ('thm-triangle-inequality','c2s4-cor-triangle-inequality','verified; independent Cauchy-Schwarz proof, all real finite dimensions including zero vectors'),
 ('c13s6-thm-curl-test-simply-connected','c17s5-thm-simply-connected-potential','statement/destination scope match; full claimed proof has LO-01 missing compactness premise'),
 ('c13s8-project-polygon','c14s7-ex-shoelace','verified; finite polygon edge calculation then supplied Green theorem; no circular reliance on the area identity')]:
 deferred.append({'from':ev(a),'destination':ev(b),'status':status})

# Original detailed schemas are retained inside each record. Partition prefixes
# make support aliases unambiguous; all physical source evidence is supplemented.
save('coverage.json',supplement({'snapshot':SNAP,'branch':INV['branch'],'source_tree_hash':INV['source_tree_hash'],'sections':records,'wrappers':wrapperrecords,'inactive_sources':INV['inactive_sources'],'inventory_issues':INV['issues'],'task_candidate_reconciliation':reconciled,'unresolved_task_candidates':bad,'review_ceiling':'Full primary semantic source read; individual dependency defects remain open, independent challenge is targeted, and most rendering is source-only.'}))
save('concept-ledger.json',supplement({'snapshot':SNAP,'capabilities':concepts,'role_conventions':'Separate typed cornerstone entries and exact definition/rule entries are retained. Null first-stage fields are unasserted or inapplicable roles, not proof of absence. Reference-route first roles are scoped to that route. Task-use edges supply additional exact uses. Do not infer that a macro or first mention supplies a capability.'}))
save('dependency-graphs.json',supplement({'snapshot':SNAP,'learning_availability':{'edges':normalized_learning,'original_review_records':learning,'support_registries':registry},'mathematical_proof':{'edges':normalized_proof,'original_review_records':proof,'supplied_roots':roots,'missing_supports':missing,'deferred_destinations':deferred},'ceiling':'Human-reconstructed capability/task edges and critical proof chains, not an exhaustive formal graph of every theorem premise or algebraic step. Entry arithmetic/calculus dependencies are named in witnesses. Deferred destinations are separate from proof-premise edges. Targeted independent cycle challenges supplement graph checks.'}))
save('task-witnesses.json',supplement({'snapshot':SNAP,'rows':normalizedtasks,'candidate_dispositions':dispositions,'candidate_reconciliation':reconciled,'counting_note':'Rows include aliases, worked prompts and report deliverables; they must not be advertised as this many distinct exercises. The 910 formal source task elements are separately reconciled.'}))
summary={'snapshot':SNAP,'active_files':len(INV['files']),'sections':len(records),'chapter_sections':sum(s['chapter']['kind']=='chapter' for s in records),'appendix_sections':sum(s['chapter']['kind']=='appendix' for s in records),'wrappers':len(wrapperrecords),'semantic_sections':sum(bool(s.get('semantic_read')) for s in records),'support_verified_sections':sum(bool(s.get('support_verified')) for s in records),'task_witness_rows':len(normalizedtasks),'formal_task_elements':sum(t['kind']=='formal' for t in TASKS),'all_inventory_candidates':len(TASKS),'unreconciled_candidates':len(bad),'capability_records':len(concepts),'learning_edges':len(learning),'proof_edges':len(proof),'changed_active_files':[p for p,h in filehash.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]}
save('evidence/integration-summary.json',summary);print(json.dumps(summary))
