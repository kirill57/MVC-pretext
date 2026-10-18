"""Check generated local HTML links, fragments, knowls, and asset references."""
import argparse
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit
from lxml import html


def inspect(root):
    root = root.resolve()
    cache, paths, files, failures, checked = {}, {}, {}, [], 0
    pages = sorted(root.glob('*.html'))

    def ids(path):
        if path not in cache:
            # Plain strings release lxml's parent-tree references between files.
            cache[path] = {str(value) for value in html.parse(str(path)).xpath('//@id')}
        return cache[path]

    for page in pages:
        tree = html.parse(str(page))
        for attribute in ('href', 'src', 'data-knowl'):
            for value in tree.xpath('//@' + attribute):
                parts = urlsplit(value)
                if parts.scheme or parts.netloc or value.startswith('/'):
                    continue
                key = (page.parent, parts.path)
                if key not in paths:
                    paths[key] = (page.parent / unquote(parts.path)).resolve() if parts.path else page
                # Empty paths refer to this particular page.
                path = paths[key] if parts.path else page
                checked += 1
                if path not in files:
                    files[path] = path.is_file()
                if not files[path]:
                    failures.append({'page': page.name, 'attribute': attribute,
                                     'reference': value, 'error': 'missing file'})
                elif parts.fragment and path.suffix == '.html' and unquote(parts.fragment) not in ids(path):
                    failures.append({'page': page.name, 'attribute': attribute,
                                     'reference': value, 'error': 'missing fragment'})
    return {'pages': len(pages), 'references_checked': checked, 'failures': failures}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    result = inspect(args.directory)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result['failures']))
