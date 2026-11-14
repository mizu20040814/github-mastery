# GitHub.com UI Mapと検証チェックリスト

基準日2026-10-26、整理日2026-11-14。**認証付きGitHub.comの実画面は全件未検証**。表はDocs由来の導線と調査候補であり、すべてが現在の画面に同時表示されると断定しない。各機能のDocs由来の場所とSource IDはfeature-inventory.csvを参照する。

| 画面 | タブ・メニュー・設定の調査対象 | 対応章 | 状態 |
|---|---|---|---|
| 全体ナビゲーション | global menu、Dashboard、Feed、検索、作成、profile menu、Notifications、Copilot、Explore/Trending | 2–4 | Docs仮説/実機未確認 |
| Profile | README、pin、repositories、contribution、achievements、status、followers、可視性 | 5 | Docs本文の概要確認/実機未確認 |
| 個人Settings・表示 | Public profile、Appearance、Accessibility、Emails、Notifications | 4–7 | Theme導線のみ詳細Docs確認、全sidebar未確認 |
| 個人Settings・保護 | Account、Password/authentication、passkeys、SSH/GPG、sessions/security log、Applications、Developer settings | 5–6、42 | 認証概念を確認/設定全項目未確認 |
| 個人Settings・費用/AI | Billing and licensing、Usage、Copilot/AI関連 | 8、36 | 最新プラン別表示未確認 |
| Repository Code | files、branch/tag、history/blame、Go to file、Add file、Code clone/download、web editor、README、About、Releases、Packages | 9–11、33 | 操作単位の追加資料照合が必要 |
| 共同作業タブ | Issues、Pull requests、Discussions、Projects、Wiki | 15–21 | 有効化・可視性・権限差未確認 |
| Pull request詳細 | Conversation、Commits、Checks、Files changed、Findings、review、merge box、stack、archive | 17–19、38 | 段階展開とプラン差を確認する |
| Actions | workflow/run/job/step/log、rerun/cancel、artifacts/cache、manual run、runners | 22–27 | 実機未確認 |
| Security/quality | policy/advisories、Dependabot、code scanning、secret scanning、dependency review、AI Scan、品質機能 | 28–32 | 名称変更と契約・enabled条件未確認 |
| Insights | Pulse、contributors、commits、code frequency、traffic、dependency graph、network、forks、community | 14、29、48 | graph概念/条件のみ確認、各画面未確認 |
| Repository Settings・General | 名前、template、default branch、feature toggles、PR/merge、archive/transfer/delete | 9、12、19 | 全設定未確認。破壊的項目は観察/設計演習 |
| Repository Settings・Rules | branches/protection、branch/tag/push rulesets、bypass、enforcement、insights | 13 | Docs概念/主な条件を確認、実機未確認 |
| Repository Settings・権限 | Collaborators/Teams、custom roles/properties、Apps、deploy keys | 12、42、44–45 | 所有者/role別導線未確認 |
| Repository Settings・実行/連携 | Actions、Runners、Secrets/Variables、Environments、Webhooks、Pages、Codespaces | 22–27、34–35、42 | 実機未確認 |
| Projects | table/board/roadmap、fields、views、filter/sort/group、workflows、insights、access | 20 | user/Org所有者差未確認 |
| Organization | Overview、Repositories、Projects、Packages、People、Teams、Security、Insights、Settings | 44–45 | owner/member/outside collaborator比較が必要 |
| Organization Settings | member privileges、roles、SSO/2FA、IP、repo defaults/rules、Actions、Apps/OAuth、AI controls、billing、audit | 44–47 | 全sidebar/契約差未確認 |
| Enterprise | Organizations、People/Teams、Policies、Security、Identity、Audit、Billing/licensing、AI controls | 46–47 | 契約/権限未確認。当面設計演習 |
| 周辺サービス | Gist、Sponsors、Education、Nonprofits、Skills/Learn、Support、Marketplace | 40、43、48 | GitHub.com外ドメインと製品UIを区別 |

## 実機調査の記録形式

UI ID / 観察日 / account種別 / plan / role / repository visibility / feature preview / viewport / URL / menu path / Feature IDs / Docsとの一致 / screenshot / 未解消事項。

1. public repositoryをログイン有無で比較し、次に本人/管理者の画面を確認する。
2. read/triage/write/maintain/admin、Org owner/member/outside collaboratorの差を利用可能な環境で確認する。
3. private、Team、GHEC、EMUは実際に利用可能な契約だけで検証し、使えない条件は未検証として残す。
4. DocsにないUIを候補追加し、Docsにあるが見えない項目は削除せず、権限・機能有効化・段階展開を調査する。
5. スクリーンショットは実画面のみ。個人情報・秘密値を除き、撮影条件と日時を記録する。

教材用MkDocsサイトのブラウザ表示確認は、GitHub.com UIの検証件数には加算しない。
