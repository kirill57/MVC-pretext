"""Check active XIncludes, IDs, references and graphics nesting; emit reading order.

This structural check does not certify pedagogical correctness or replace the
PreTeXt schema/build. Run from any directory with Python and lxml installed.
"""
from pathlib import Path
from collections import Counter
import json
import re
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[1]
XI = '{http://www.w3.org/2001/XInclude}include'
ID = '{http://www.w3.org/XML/1998/namespace}id'
files, sections, ids, refs, errors = [], [], {}, [], []


def visit(path, ancestors=()):
    path = path.resolve()
    if path in ancestors:
        raise ValueError(f'XInclude cycle: {path}')
    tree = ET.parse(str(path))
    rel = path.relative_to(ROOT).as_posix()
    files.append(rel)
    for node in tree.iter():
        if node.tag == XI:
            if node.get('xpointer') or node.get('parse', 'xml') != 'xml':
                raise ValueError(f'Unsupported include mode: {rel}:{node.sourceline}')
            visit(path.parent / node.get('href'), (*ancestors, path))
        ident = node.get(ID)
        if ident:
            if ident in ids:
                errors.append(f'Duplicate ID {ident}: {ids[ident]} / {rel}:{node.sourceline}')
            ids[ident] = f'{rel}:{node.sourceline}'
        if node.tag == 'section':
            sections.append({'order': len(sections)+1, 'path': rel,
                             'id': ident, 'title': ''.join(node.find('title').itertext())})
        if node.tag == 'xref':
            for attr in ('ref', 'first', 'last'):
                for ref in re.split(r'[,\s]+', node.get(attr, '').strip()):
                    if ref:
                        refs.append((ref, rel, node.sourceline))
        if node.tag in ('latex-image', 'asymptote') and node.getparent().tag != 'image':
            errors.append(f'Graphics outside image: {rel}:{node.sourceline}')


visit(ROOT / 'source/main.ptx')
for ref, path, line in refs:
    if ref not in ids:
        errors.append(f'Unresolved reference {ref}: {path}:{line}')
for path, count in Counter(files).items():
    if count > 1:
        errors.append(f'File included {count} times: {path}')
all_sources = {p.relative_to(ROOT).as_posix() for p in (ROOT/'source').rglob('*')
               if p.suffix in ('.xml', '.ptx')}
record = {'active_files': files, 'sections': sections,
          'inactive_files': sorted(all_sources-set(files)), 'id_count': len(ids),
          'reference_count': len(refs), 'errors': errors}
(ROOT/'logs').mkdir(exist_ok=True)
(ROOT/'logs/prerequisite-structure.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
print(f'{len(files)} active files; {len(sections)} sections; {len(ids)} IDs; {len(refs)} references')
print(f'{len(record["inactive_files"])} inactive XML/PTX files; {len(errors)} structural errors')
for error in errors:
    print(error)
raise SystemExit(bool(errors))
