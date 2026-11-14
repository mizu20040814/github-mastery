# Docs分類と調査経路

基準日2026-10-26、入口再確認2026-11-14。[GitHub Docsトップ](https://docs.github.com/en)（SRC-REP-001）の群を教材へ対応づけた。下表は入口の分類であり、全リンク先・全下位ページを本文確認した意味ではない。

| Docsの群 | 下位入口と調査対象 | 主な章 | 未完了の境界 |
|---|---|---|---|
| Get started | Get started、Migrations、Account/profile、Notifications、Authentication、Billing、Site policy | 1–8、9、46、48 | 全記事・移行経路・全設定と規約 |
| Collaborative coding | Codespaces、Repositories、Pull requests、Discussions、Integrations | 9–21、35、43 | 全タブ/操作/設定・権限差 |
| GitHub Copilot | Plans、Cloud agent、Tutorials、Cookbook、Customization、CLI | 36–40、47 | 全モデル・クライアント・料金・履歴 |
| CI/CD and DevOps | Actions、Packages、Pages | 22–27、33–35 | 全events/構文/Runner/registry/制限 |
| Security and code quality | Secrets、Code vulnerabilities、Supply chain、Code quality、Secure at scale | 28–32、45、47 | 全alert/管理設定・契約差 |
| Client apps | CLI、Mobile、Desktop | 40 | GitHub.comとの関係を補足。固有機能は別範囲 |
| Project management | Issues、Projects、Search | 3、15–16、20 | 全fields/views/検索/自動化 |
| Enterprise and teams | Organizations、Secure at scale、Onboarding、Enterprise administrators | 44–47 | IdP/契約/権限別検証、GHES差分 |
| Developers | Apps、REST、GraphQL、Webhooks | 40–43 | 全endpoint/schemaと認証フロー |
| Community | Communities、Sponsors、Education、Nonprofits、Support、Contribute to Docs | 48 | 資格/地域/税/モデレーション |
| More docs | CodeQL query、Electron、npm、Well-Architected | 30、32、43、50 | 外部製品の資料。関係分類のみ |

## 集計方法

登録資料の分類と件数はsource-catalog.csvを正とする。機能の一意IDはfeature-inventory.csvで管理する。機能数、開いたページ数、カテゴリ入口の表示記事数は別の指標であり、足し合わせない。今回の選定資料集合には未発見・未収集のDocsが含まれないため、GitHub全体の網羅率を出さない。

## 次回の収集単位

各カテゴリのページ送りを最後まで巡回し、発見元URL、親カテゴリ、候補URL、最終URL、対象製品、取得状態、本文読解状態、対応Feature IDを残す。URL取得成功だけで「本文確認済み」に昇格させない。1ページが複数機能を扱う場合はSource IDを共有し、重複登録を避ける。

旧URLのredirect、取得失敗、廃止機能も履歴として残す。基準日より後の変更は現行差分として分離し、日付のないDocsから過去時点を推定しない。
