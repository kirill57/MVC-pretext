from pathlib import Path
import json,hashlib,collections
root=Path(__file__).resolve().parents[4]
out=Path(__file__).parent
load=lambda p:json.loads(p.read_text(encoding='utf8'))
idx=load(root/'audit/logical-order-round2/id-index.json')
tasks=load(root/'audit/logical-order-round2/task-inventory.json')
assigned=[t for t in tasks if 1<=(t.get('section_order') or 0)<=56]
rows=load(out/'task-witnesses.json'); graph=load(out/'graphs.json')
coverage=load(out/'coverage.json'); candidates=load(out/'candidate-dispositions.json')
errors=[]; hashes={}; edges_checked=0
def check_ev(e):
    if not e:return
    p=e.get('path')
    if not p:return
    if p not in hashes:hashes[p]=hashlib.sha256((root/p).read_bytes()).hexdigest()
    if hashes[p]!=e['sha256']:errors.append('hash mismatch '+p)
    if 'lines' in e and not (1<=e['lines'][0]<=e['lines'][1]):errors.append('bad lines '+repr(e))
formal={r['task_id'] for r in rows if r['kind']=='formal'}
expected={t['task_key'] for t in assigned if t['kind']=='formal'}
if formal!=expected:errors.append('formal identity mismatch '+repr(formal^expected))
if len({r['task_id'] for r in rows})!=len(rows):errors.append('duplicate witness identity')
if {r['task_id'] for r in candidates}!={t['task_key'] for t in assigned if t['kind']!='formal'}:errors.append('candidate identity mismatch')
for row in rows:
    check_ev(row['evidence'])
    if not row['solution_outline'].strip() or not row['support_ids']:errors.append('empty witness '+row['task_id'])
for edge in graph['learning_edges']:
    edges_checked+=1
    s=edge['source'];a=edge['source_evidence'];b=edge['target_evidence']
    if s!='ENTRY' and s not in idx and s not in graph['support_nodes']:errors.append('unresolved support '+s)
    check_ev(a);check_ev(b)
    if a:
        ao,bo=a.get('section_order'),b.get('section_order')
        if ao is not None and bo is not None and ao>bo:errors.append('future support '+s+' -> '+edge['target'])
        if ao==bo and a['lines'][0]>b['lines'][0]:errors.append('later same-section support '+s+' -> '+edge['target'])
for c in coverage:check_ev(c.get('evidence',c))
report={'snapshot':graph['snapshot'],'sections':56,'coverage_records':len(coverage),'formal_tasks':len(formal),'additional_tasks':len(rows)-len(formal),'candidate_dispositions':len(candidates),'learning_edges_checked':edges_checked,'source_files_hash_verified':len(hashes),'errors':errors,'scope':'Record identity/provenance/ordering checks only. Mathematical verification is the manual source and solution pass, not this script.'}
(out/'validation.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps(report,indent=2))
assert not errors
