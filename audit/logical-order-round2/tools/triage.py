"""Analyze explicit reviewer annotations, never infer teaching from words/macros.

This is fixture/consistency infrastructure, not a semantic auditor. Capabilities,
sufficiency, proof edges and status must be assigned by a human reader.
"""
def available(use,supports):
 return any(s['capability']==use['capability'] and s.get('sufficient',False)
            and s['order']<=use['order'] and s.get('visible',True)
            and (not s.get('optional',False) or use.get('optional',False))
            for s in supports)
def issues(uses,supports):
 return [u['id'] for u in uses if not u.get('optional',False) and not available(u,supports)]
def cycles(edges):
 graph={}
 for a,b in edges:graph.setdefault(a,[]).append(b)
 active=set();done=set();found=[]
 def walk(x,path):
  if x in active:found.append(path[path.index(x):]+[x]);return
  if x in done:return
  active.add(x)
  for y in graph.get(x,[]):walk(y,path+[x])
  active.remove(x);done.add(x)
 for x in graph:walk(x,[])
 return found
