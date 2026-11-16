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
# 総合演習で使う機能は、個人/チームと大規模/AIの目的から選ぶ。
LAB_FEATURES = {
 49: 'GH-REP-042 GH-REP-003 GH-REP-013 GH-COL-001 GH-COL-023 GH-COL-027 GH-COL-030 GH-COL-010 GH-ACT-001 GH-ACT-033 GH-ACT-052 GH-ACT-060 GH-AI-020 GH-AI-025 GH-AI-032'.split(),
 50: 'GH-AI-003 GH-AI-008 GH-AI-013 GH-AI-015 GH-AI-017 GH-AI-018 GH-AI-034 GH-AI-035 GH-AI-036 GH-AI-048 GH-AI-054 GH-AI-055 GH-ACT-014 GH-ACT-017 GH-ACT-019 GH-ACT-025 GH-ACT-037 GH-ACT-044 GH-ACT-049 GH-ACT-063'.split(),
}
def reused_features(number, features):
 if number in LAB_FEATURES: return LAB_FEATURES[number]
 categories = {12: {'Repositories','Actions','Security'}, 28: {'Security'}}
 return [f['feature_id'] for f in features if f['category'] in categories.get(number, set())]
def main():
 fs,ss,gs=collect()
 for name,rows,fields in [('feature-inventory',fs,FF),('source-catalog',ss,SF)]:
  with (ROOT/f'research/{name}.csv').open('w',newline='') as h:
   w=csv.DictWriter(h,fields,lineterminator='\n');w.writeheader();w.writerows(rows)
 cs=json.loads((ROOT/'plans/chapters.json').read_text());lines=['# 機能と章の対応','']
 for c in cs:
  ids=[f['feature_id'] for f in fs if str(c['number']) in split(f['related_chapter'])];c['feature_ids']=ids
  reused=reused_features(c['number'],fs);c['reused_feature_ids']=reused
  lines += [f'<a id="ch-{c["number"]:02}"></a>', '',f'## 第{c["number"]}章 {c["title"]}', '',f'[学習設計](detailed-toc.md#ch-{c["number"]:02})','', '直接対応: '+(', '.join(ids) or 'なし'), '']
  if reused: lines += ['再利用: '+', '.join(reused),'']

 (ROOT/'plans/chapters.json').write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'plans/feature-chapter-map.md').write_text('\n'.join(lines))
 m={'reference_date':'2026-10-26','checked_on':'2026-11-14','features':len(fs),'sources':len(ss),'unique_urls':len({s['url'].rstrip('/') for s in ss}),'source_states':dict(Counter(s['verification_status'] for s in ss)),'docs_opened':len({s['url'].rstrip('/') for s in ss if s['source_type']=='Docs' and s['verification_status']=='opened'}),'categories':dict(Counter(f['category'] for f in fs)),'ui_verified':sum(f['ui_verification_status']=='verified' for f in fs),'practical_verified':sum(f['practical_verification_status']=='verified' for f in fs),'parts':12,'chapters':len(cs)}
 (ROOT/'audits/metrics.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'research/research-gaps.md').write_text('# 調査残課題\n\n基準2026-10-26、再確認2026-11-14。全Docs巡回と認証付きUIは未完了。\n\n'+'\n'.join('- '+g for g in gs)+'\n')
 print(json.dumps(m,ensure_ascii=False))
if __name__=='__main__':main()
