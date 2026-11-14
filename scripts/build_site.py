#!/usr/bin/env python3
"""Stage managed Markdown and CSV sources and run MkDocs strict build."""
from pathlib import Path
import argparse
import csv
import html
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
STAGING=ROOT/'.build/docs'

def stage():
    if STAGING.exists(): shutil.rmtree(STAGING)
    STAGING.mkdir(parents=True)
    for name in ('docs','research','plans','labs','case-studies','quizzes','audits','assets'):
        base=ROOT/name
        if not base.exists(): continue
        for source in base.rglob('*'):
            if source.is_file() and source.suffix in {'.md','.csv','.json','.png','.svg','.jpg','.js','.txt'}:
                target=STAGING/source.relative_to(ROOT)
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(source,target)
    for name in ('README.md','CHANGELOG.md','AGENTS.md'):
        if (ROOT/name).exists(): shutil.copyfile(ROOT/name,STAGING/('project-readme.md' if name=='README.md' else name))
    home=(ROOT/'docs/index.md').read_text().replace('](../','](')
    (STAGING/'index.md').write_text(home)
    for name,title,key in [('feature-inventory','機能台帳','feature_id'),('source-catalog','公式出典台帳','source_id')]:
        path=STAGING/'research'/f'{name}.csv'
        with path.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
        lines=[f'# {title}','','research/fragments/*.jsonを修正し、統合スクリプトでCSVを再生成してください。', '',f'[CSV原本]({name}.csv)', '', f'登録{len(rows)}件。全GitHub機能の網羅率ではありません。','']
        for row in rows:
            identifier=row[key]
            lines += [f'## {identifier} {{#{identifier.lower()}}}','','| 項目 | 内容 |','|---|---|']
            for k,v in row.items():
                raw=v or '（記録なし）'
                v=html.escape(raw).replace('|','&#124;').replace('\n','<br>')
                if raw.startswith('https://') and ' ' not in raw: v=f'<{raw}>'
                elif k=='source_ids': v='; '.join(f'[{x}](source-catalog.md#{x.lower()})' for x in raw.split(';') if x)
                elif k=='related_features' and raw!='（記録なし）': v='; '.join(f'[{x}](feature-inventory.md#{x.lower()})' for x in raw.split(';') if x)
                elif k=='related_chapter': v='; '.join(f'[第{x}章](../plans/detailed-toc.md#ch-{int(x):02})' for x in raw.split(';') if x.isdigit())
                lines.append(f'| {k} | {v} |')
            lines.append('')
        path.with_suffix('.md').write_text('\n'.join(lines)+'\n')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--stage-only',action='store_true');args=parser.parse_args()
    stage()
    if not args.stage_only: subprocess.run([sys.executable,'-m','mkdocs','build','--strict'],cwd=ROOT,check=True)
if __name__=='__main__': main()
