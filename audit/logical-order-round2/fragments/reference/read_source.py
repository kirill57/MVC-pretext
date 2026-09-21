from pathlib import Path
from lxml import etree as E
import sys,re
ROOT=Path(__file__).resolve().parents[4]
X='{http://www.w3.org/XML/1998/namespace}id'
BLOCKS={'p','md','mdn','title','cell','latex-image','asymptote','caption','description','li'}
def read(p):
 print('\nFILE',str(p.relative_to(ROOT)).replace('\\','/'))
 tree=E.parse(str(p))
 for e in tree.iter():
  if not isinstance(e.tag,str): continue
  tag=E.QName(e).localname
  if tag in {'section','subsection','exercise','theorem','proposition','lemma','definition','example','proof','hint','solution','project','task','remark','warning','aside'}:
   print(f'{e.sourceline} <{tag}> {e.get(X,"")}')
  if tag in BLOCKS and not any(E.QName(a).localname in BLOCKS for a in e.iterancestors() if isinstance(a.tag,str)):
   s=E.tostring(e,encoding='unicode',method='text')
   if tag not in {'latex-image','asymptote'}: s=re.sub(r'\s+',' ',s).strip()
   print(f'{e.sourceline}: {s}')
for arg in sys.argv[1:]:
 p=ROOT/arg
 if p.is_dir():
  wrapper=next(p.glob('*.ptx'))
  t=E.parse(str(wrapper))
  for e in t.findall('{http://www.w3.org/2001/XInclude}include'): read(p/e.get('href'))
 else: read(p)
