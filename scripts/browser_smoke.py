#!/usr/bin/env python3
"""Optional Chromium checks for the generated MkDocs site, using Playwright."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import threading,json,os
from datetime import datetime,timezone
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT/'site')))
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}'
results=[];errors=[];requests=[]
out=ROOT/'assets/screenshots';out.mkdir(parents=True,exist_ok=True)
def check(name,fn):
 try:fn();results.append({'name':name,'status':'passed'})
 except Exception as e:results.append({'name':name,'status':'failed','detail':str(e)[:500]})
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000},locale='ja-JP')
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.on('requestfailed',lambda r:requests.append(r.url))
 page.goto(base,wait_until='networkidle')
 def home():assert page.locator('h1').inner_text().startswith('GitHub完全習得プロジェクト')
 def mermaid():
  client=page.context.new_cdp_session(page)
  doc=client.send('DOM.getDocument',{'depth':-1,'pierce':True})
  def walk(n):
   return n.get('nodeName','').lower()=='svg' or any(walk(c) for k in ('children','shadowRoots') for c in n.get(k,[]))
  assert walk(doc['root'])
 def search():
  q=page.locator('[data-md-component="search-query"]');q.click();q.fill('機能台帳');q.press('ArrowRight')
  page.locator('.md-search-result__item').first.wait_for(state='visible',timeout=20000)
  page.screenshot(path=str(out/'site-search-desktop.png'));page.keyboard.press('Escape')
 check('desktop_home',home);check('mermaid_svg',mermaid)
 page.screenshot(path=str(out/'site-home-desktop.png'))
 check('japanese_search',search)
 phone=browser.new_page(viewport={'width':390,'height':844},is_mobile=True,locale='ja-JP');phone.goto(base,wait_until='networkidle')
 def mobile():
  assert phone.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
  phone.locator('header label[for="__drawer"]').first.click();assert phone.locator('#__drawer').is_checked()
  phone.screenshot(path=str(out/'site-menu-mobile.png'))
 check('mobile_menu',mobile)
 version=browser.version;browser.close()
server.shutdown();server.server_close()
report={'checked_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'MkDocs教材サイトのみ。GitHub.comのUI・実践演習は未検証。','browser':version,'checks':results,'page_errors':errors,'failed_requests':requests,'limitations':'単一Chromium、1440px/390pxのsmoke確認。全端末・全検索語・アクセシビリティ適合は未確認。'}
(ROOT/'audits/browser-smoke.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(any(r['status']!='passed' for r in results) or bool(errors) or bool(requests))
