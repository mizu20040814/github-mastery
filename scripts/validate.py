#!/usr/bin/env python3
"""Check research integrity, chapter dependencies, internal links and CI."""
import csv,json,re,sys
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from pathlib import Path
import markdown,yaml
from integrate_research import ROOT,FF,SF,collect,split
from build_site import stage,STAGING
errors=[]
def ck(ok,msg):
 if not ok:errors.append(msg)
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='a' and 'href'in a:self.links.append(a['href'])
  if tag=='img' and 'src'in a:self.links.append(a['src'])
def main():
 rows=[]
 for name,fields in [('feature-inventory',FF),('source-catalog',SF)]:
  with (ROOT/f'research/{name}.csv').open(newline='') as h:
   r=csv.DictReader(h);ck(r.fieldnames==fields,f'{name}: schema');data=list(r)
  ck(all(None not in x and None not in x.values() for x in data),f'{name}: malformed CSV');rows.append(data)
 fs,ss=rows;ef,es,_=collect();ck(fs==ef and ss==es,'stale CSV')
 fids={f['feature_id'] for f in fs};sids={s['source_id'] for s in ss}
 ck(len(fids)==len(fs),'duplicate Feature ID');ck(len(sids)==len(ss),'duplicate source ID')
 ck(len({s['url'].rstrip('/') for s in ss})==len(ss),'duplicate source URL')
 sources={s['source_id']:s for s in ss}
 cs=json.loads((ROOT/'plans/chapters.json').read_text());nums={c['number'] for c in cs};ck(nums==set(range(1,51)) and len(cs)==50,'50 unique chapters required')
 done=set()
 for _ in cs:done|={c['number'] for c in cs if set(c['prerequisites'])<=done}
 ck(done==nums,'chapter dependency cycle')
 for f in fs:
  fid=f['feature_id'];refs=split(f['source_ids'])
  ck(bool(refs) and set(refs)<=sids,f'{fid}: source references')
  ck(set(split(f['related_features']))<=fids,f'{fid}: related references')
  ck(bool(f['related_chapter']) and set(split(f['related_chapter']))<=set(map(str,nums)),f'{fid}: chapter references')
  ck(f['official_documentation_url'] in {sources[s]['url'] for s in refs if s in sources},f'{fid}: URL not in source references')
  if f['documentation_verification_status']=='verified':ck(any(sources.get(s,{}).get('verification_status')=='opened' for s in refs),f'{fid}: no opened evidence')
 for s in ss:ck(bool(s['category']) and bool(s['url']),f'{s["source_id"]}: unclassified')
 stage();parsed={}
 for p in Path(STAGING).rglob('*.md'):
  parser=Parser();parser.feed(markdown.markdown(p.read_text(),extensions=['extra','toc','pymdownx.superfences']));parsed[p.resolve()]=parser
 count=0
 for p,parser in parsed.items():
  for href in parser.links:
   u=urlsplit(href)
   if u.scheme or u.netloc:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p
   ck(target.exists(),f'{p.relative_to(STAGING)}: missing {href}')
   if target in parsed and u.fragment:ck(unquote(u.fragment) in parsed[target].ids,f'{p.relative_to(STAGING)}: missing anchor {href}')
   count+=1
 w=yaml.load((ROOT/'.github/workflows/docs.yml').read_text(),Loader=yaml.BaseLoader)
 ck(w.get('permissions')=={'contents':'read'},'workflow permissions')
 for job in w.get('jobs',{}).values():
  for step in job.get('steps',[]):
   if 'uses'in step:ck(bool(re.fullmatch(r'[^@]+@[a-f0-9]{40}',step['uses'])),'action must use SHA')
 result={'result':'failed' if errors else 'passed','features':len(fs),'sources':len(ss),'chapters':len(cs),'markdown_files':len(parsed),'local_links_checked':count,'errors':errors}
 (ROOT/'audits/validation-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(errors))
if __name__=='__main__':main()
