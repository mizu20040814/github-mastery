#!/usr/bin/env python3
"""Generate research CSV and mappings from reviewed JSON fragments."""
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FF='feature_id category subcategory feature_name description ui_location official_documentation_url product_plan_availability required_permissions availability_status documentation_verification_status ui_verification_status practical_verification_status last_verified_date related_chapter related_features notes source_ids'.split()
SF='source_id url title source_type category verification_status checked_on published_on evidence notes'.split()
def split(s):return [v.strip() for v in s.split(';') if v.strip()]
def collect():
 fs=[];ss=[];gs=[]
 for p in sorted((ROOT/'research/fragments').glob('*.json')):
  d=json.loads(p.read_text());fs+=d['features'];ss+=d['sources'];gs += [f'{p.stem}: {g}' for g in d.get('gaps',[])]
 return sorted(fs,key=lambda f:f['feature_id']),sorted(ss,key=lambda s:s['source_id']),gs
def main():
 fs,ss,gs=collect()
 for name,rows,fields in [('feature-inventory',fs,FF),('source-catalog',ss,SF)]:
  with (ROOT/f'research/{name}.csv').open('w',newline='') as h:
   w=csv.DictWriter(h,fields,lineterminator='\n');w.writeheader();w.writerows(rows)
 cs=json.loads((ROOT/'plans/chapters.json').read_text());lines=['# 機能と章の対応','']
 for c in cs:
  ids=[f['feature_id'] for f in fs if str(c['number']) in split(f['related_chapter'])];c['feature_ids']=ids
  if c['number'] in (12,28,49,50):c['reused_feature_ids']=[f['feature_id'] for f in fs if (c['number']==12 and f['category'] in ('Repositories','Actions','Security')) or (c['number']==28 and f['category']=='Security') or (c['number']==49 and any(int(n)<36 for n in split(f['related_chapter']))) or (c['number']==50 and any(int(n)>=22 for n in split(f['related_chapter'])))]
  lines += [f'<a id="ch-{c["number"]:02}"></a>', '',f'## 第{c["number"]}章 {c["title"]}', '',f'[学習設計](detailed-toc.md#ch-{c["number"]:02})','',', '.join(ids) or '総覧・総合演習：既存機能を再利用（chapters.json参照）。','']
 (ROOT/'plans/chapters.json').write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'plans/feature-chapter-map.md').write_text('\n'.join(lines))
 m={'reference_date':'2026-10-26','checked_on':'2026-11-14','features':len(fs),'sources':len(ss),'unique_urls':len({s['url'].rstrip('/') for s in ss}),'source_states':dict(Counter(s['verification_status'] for s in ss)),'docs_opened':len({s['url'].rstrip('/') for s in ss if s['source_type']=='Docs' and s['verification_status']=='opened'}),'categories':dict(Counter(f['category'] for f in fs)),'ui_verified':sum(f['ui_verification_status']=='verified' for f in fs),'practical_verified':sum(f['practical_verification_status']=='verified' for f in fs),'parts':12,'chapters':len(cs)}
 (ROOT/'audits/metrics.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'research/research-gaps.md').write_text('# 調査残課題\n\n基準2026-10-26、再確認2026-11-14。全Docs巡回と認証付きUIは未完了。\n\n'+'\n'.join('- '+g for g in gs)+'\n')
 print(json.dumps(m,ensure_ascii=False))
if __name__=='__main__':main()
