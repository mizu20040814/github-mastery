# サイト基盤の検証

復元・検証日: **2026-11-14**。教材の調査基準日: **2026-10-26**。

## 実装

- MkDocs 1.6.1 / Material 9.6.21 / pymdown-extensions 10.16.1 / PyYAML 6.0.3を直接依存として固定し、解決した推移依存をrequirements-lock.txtに固定した。
- 日本語・英語検索、コード表示、Mermaid、12部の案内と50章の詳細目次への導線を実装した。
- 原本はresearch/plans等の管理場所に置き、scripts/build_site.pyが.build/docsへ配置する。CSV閲覧ページはビルド時に生成する。
- READMEはproject-readme.mdとして配置しトップindexとの出力競合を避ける。
- Mermaid 11.12.0の公式npm配布を固定して同梱し、MITライセンスとSHA256を保存した。外部CDNからの読み込みに依存しない。
- GitHub Actionsはcontents: read、ActionはSHA固定、checkoutの認証情報永続化を無効にした。公開・デプロイ処理は含まない。

## 実行結果

| 検証 | 結果 | 根拠・限界 |
|---|---|---|
| 依存インストール | 成功 | Python 3.12の.venvへ固定直接依存をインストール |
| 推移依存の整合性 | 成功 | pip check: No broken requirements found |
| Python構文 | 成功 | build_site.py / browser_smoke.pyをpy_compileで確認 |
| MkDocs strict build | 成功 | 最新統合資料で実行、警告0、0.94秒 |
| Desktop表示 | 成功 | Chromium 154.0.8037.57、1440×1000 |
| 日本語検索 | 成功 | 「機能台帳」で検索結果の表示を確認 |
| Mermaid | 成功 | 実描画のSVGをCDPのshadow DOMを含む検査で確認 |
| Mobile表示・ナビ | 成功 | 390×844、ページ全体の横はみ出しなし、メニューを開ける |
| ブラウザエラー | 0 | page_errors / failed_requestsとも空 |
| GitHub Actions runner | この記録では未確認 | push後の実行結果は親の監査に記録 |

実結果は[browser-smoke.json](browser-smoke.json)。初回strict buildは他担当の未完成文書・章対応アンカー不足を検出し、統合後に再実行して成功した。ブラウザ初回のh1完全一致・Mermaidのdata属性・日本語入力イベントの検査条件は実表示に合わず修正した。最終結果は上表のとおり。

スクリーンショットは実際に生成したMkDocsサイトの画面であり、GitHub.comの認証付きUIを検証した証拠ではない。

- [Desktop画面](../assets/screenshots/site-home-desktop.png)
- [日本語検索](../assets/screenshots/site-search-desktop.png)
- [Mobileメニュー](../assets/screenshots/site-menu-mobile.png)

## 再現

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build_site.py
python scripts/browser_smoke.py
```

最後の表示確認はPlaywrightとChromiumがある検証環境で実行する（今回のmanaged runtimeにはPlaywright 1.62.0と/usr/bin/chromiumが利用可能）。単一ブラウザと2画面幅のsmoke testであり、全端末・アクセシビリティ適合性・全検索語の確認を意味しない。GitHub.comの製品UIと実践演習は別途未検証として管理する。
