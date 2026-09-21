from pathlib import Path
from lxml import etree as E
import sys,re,json
ROOT=Path(__file__).resolve().parents[4]
NS={'xi':'http://www.w3.org/2001/XInclude'}
files=[]
for p in sorted((ROOT/'source/chapters').glob('ch0[1-8]*/*.ptx')):
 for n in E.parse(str(p)).xpath('//xi:include',namespaces=NS): files.append(p.parent/n.get('href'))
start=int(sys.argv[1]); stop=int(sys.argv[2]) if len(sys.argv)>2 else start+1
for i in range(start,stop):
 p=files[i]; tree=E.parse(str(p)); root=tree.getroot()
 print('\nFILE',i,p.relative_to(ROOT),root.get('{http://www.w3.org/XML/1998/namespace}id'))
 for n in root.iter():
  if not isinstance(n.tag,str):continue
  tag=E.QName(n).localname
  if tag in ['title','p','md','mdn','me','men','mrow','caption','description','latex-image','asymptote','li','cell'] and not any(E.QName(a).localname in ['p','md','mdn','me','men','caption','description','latex-image','asymptote','li','cell'] for a in n.iterancestors()):
   txt=' '.join(''.join(n.itertext()).split()); refs=[x.get('ref') for x in n.iter('xref')]; txt += (' [XREF '+','.join(refs)+']') if refs else ''
   if tag in ['latex-image','asymptote']:
    txt='GRAPHIC SOURCE '+txt
   ident=n.get('{http://www.w3.org/XML/1998/namespace}id') or next((a.get('{http://www.w3.org/XML/1998/namespace}id') for a in n.iterancestors() if a.get('{http://www.w3.org/XML/1998/namespace}id')),None)
   print(f'{n.sourceline} [{tag}/{ident}] {txt}')

