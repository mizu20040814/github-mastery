# 章別制作計画

更新2026-11-14。学習順と制作順は異なる。認証・Repository・PR・Actionsを前提依存に従って検証する。

| 制作順 | 章 | 前提 | 出典調査軸 | レビュー |
|---|---|---|---|---|
| 1 | [第1章 GitとGitHubの仕組み](detailed-toc.md#ch-01) |  | Get started、Git公式 | 小さなcommitと参照の移動を図示する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 2 | [第2章 GitHub.comの全体構造](detailed-toc.md#ch-02) | 1 | Get started、Account、Repositories | 公開閲覧とログイン時の導線を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 3 | [第3章 GitHubの検索機能](detailed-toc.md#ch-03) | 2 | Search、REST Search | 既知の対象を使いヒットと非ヒットを説明する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 4 | [第4章 GitHubの画面操作と表示](detailed-toc.md#ch-04) | 2 | Account、Accessibility、Writing | キーボードだけでIssueを探し表示差を記録する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 5 | [第5章 AccountとProfile](detailed-toc.md#ch-05) | 2 | Account and profile | 本人と公開閲覧のプロフィールを比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 6 | [第6章 認証とアカウント保護](detailed-toc.md#ch-06) | 1,5 | Authentication、Apps | 読取専用認証と失効時の動作を確認する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 7 | [第7章 NotificationsとSubscriptions](detailed-toc.md#ch-07) | 2,5 | Subscriptions and notifications | レビュー依頼とmentionの通知を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 8 | [第8章 Billingと利用プラン](detailed-toc.md#ch-08) | 5 | Billing、Plans | 無料枠と従量項目を出典日付きで試算する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 9 | [第9章 Repositoryの作成と管理](detailed-toc.md#ch-09) | 1,6 | Repositories、Migrations | 使い捨てRepositoryを作り所有と可視性を説明する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 10 | [第10章 Codeタブの全機能](detailed-toc.md#ch-10) | 1,9 | Repositories、Code navigation | 固定commitのpermalinkと変更PRを作成する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 11 | [第11章 ブランチ・コミット管理](detailed-toc.md#ch-11) | 1,9,10 | Repositories、Authentication、Git | 作業branchとtagを作り差分を検証する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 12 | [第12章 RepositoryのSettings](detailed-toc.md#ch-12) | 8,9 | Repositories、Actions、Organizations | readとadminで設定の見え方を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 13 | [第13章 Rulesetsとブランチ保護](detailed-toc.md#ch-13) | 11,12 | Rulesets、Protected branches | 承認とcheckの成功・拒否ケースを設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 14 | [第15章 GitHub Issues](detailed-toc.md#ch-15) | 3,9 | Issues、Issue forms | 不具合テンプレートから課題を登録する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 15 | [第17章 Pull Requestの全体像](detailed-toc.md#ch-17) | 11,15 | Pull requests、Issues | IssueからDraft PRを作りレビュー準備をする。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 16 | [第14章 InsightsとRepository分析](detailed-toc.md#ch-14) | 9,15,17 | Repositories Insights、Community | 観測期間と権限を固定した分析を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 17 | [第18章 Code Reviewの完全解説](detailed-toc.md#ch-18) | 13,17 | Pull requests reviews、CODEOWNERS | 担当所有者のレビューと修正を循環させる。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 18 | [第21章 Discussionsと共同作業](detailed-toc.md#ch-21) | 9,15,17 | Discussions、Wiki、Community | 質問から回答とWiki記録へつなぐ。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 19 | [第22章 GitHub Actionsの基本](detailed-toc.md#ch-22) | 9,11,17 | Actions quickstart、Concepts | 成功と失敗するテストCIを作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 20 | [第19章 PRのマージと変更履歴](detailed-toc.md#ch-19) | 13,18,22 | Pull requests、Merge queue、Actions | 同じ変更を各方式で統合し履歴を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 21 | [第23章 Workflowの詳細仕様](detailed-toc.md#ch-23) | 22 | Workflow syntax、Events、Contexts | イベントごとのrefとtoken条件を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 22 | [第24章 Actionsの高度な設計](detailed-toc.md#ch-24) | 23 | Actions reuse、Cache、Artifacts | cache有無の同等性と再利用境界を確認する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 23 | [第27章 Actionsのセキュリティ](detailed-toc.md#ch-27) | 6,23 | Actions security、OIDC | 秘密値なしの入力で境界を検証する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 24 | [第25章 Runnerと実行環境](detailed-toc.md#ch-25) | 23,27 | Actions runners、ARC | 信頼境界と実行環境の比較表を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 25 | [第26章 CDとデプロイ](detailed-toc.md#ch-26) | 23,27 | Environments、Deployments、OIDC | 本番公開せず承認付き配送の状態遷移を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 26 | [第28章 Securityタブの全体構造](detailed-toc.md#ch-28) | 8,12 | Security and quality、Billing | 検出機能と契約・権限の表を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 27 | [第29章 Dependabotと依存関係](detailed-toc.md#ch-29) | 22,28 | Supply chain、Dependabot | 更新PRと導入差分検査を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 28 | [第30章 Code Security](detailed-toc.md#ch-30) | 23,28 | Code scanning、CodeQL、Quality | 検証用コードで検出と修正結果を照合する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 29 | [第31章 Secret Security](detailed-toc.md#ch-31) | 6,28 | Secret scanning、Push protection | 本物の秘密値を使わず対応手順を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 30 | [第32章 サプライチェーンと品質統制](detailed-toc.md#ch-32) | 13,24,29,30,31 | Supply chain、Attestations、Rulesets | 署名有無と検証条件成立の違いを評価する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 31 | [第33章 Releases・Packages・Registry](detailed-toc.md#ch-33) | 11,24,32 | Releases、Packages、GHCR | 未公開のrelease案と配布物digestを作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 32 | [第34章 GitHub Pages](detailed-toc.md#ch-34) | 8,22,26 | Pages、Actions deployment | ローカル相当の生成サイトを検証し公開手順を記す。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 33 | [第35章 GitHub Codespaces](detailed-toc.md#ch-35) | 8,9,25 | Codespaces、Dev Containers、Billing | 設定ファイルと実環境の確認項目を分ける。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 34 | [第36章 GitHub.com上のCopilot](detailed-toc.md#ch-36) | 6,8,10 | Copilot、Plans、Changelog | 回答の根拠と人間の検証手順を記録する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 35 | [第37章 Copilot Cloud Agent](detailed-toc.md#ch-37) | 17,22,27,36 | Cloud agent、Sessions、Actions | 小さなIssueに対する変更案を人間が評価する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 36 | [第38章 Copilot Code Review](detailed-toc.md#ch-38) | 18,36 | Copilot code review、PR reviews | AIが指摘しない問題も含めレビューを採点する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 37 | [第40章 GitHub CLIと周辺ツール](detailed-toc.md#ch-40) | 1,6,17 | CLI manual、Desktop、Mobile | 同じPRをWebと読取CLIで比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 38 | [第41章 GitHub API](detailed-toc.md#ch-41) | 6,15,17,40 | REST、GraphQL、Authentication | 読取APIの複数ページと失敗応答を処理する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 39 | [第42章 GitHub AppsとWebhooks](detailed-toc.md#ch-42) | 6,41 | Apps、Webhooks、OAuth | fixtureで署名と冪等処理を検証する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 40 | [第39章 AIエージェント連携と統制](detailed-toc.md#ch-39) | 27,37,38,42 | Copilot customization、MCP、各ベンダー公式 | IssueからCI・人間承認までの責任分担を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 41 | [第43章 外部サービス連携](detailed-toc.md#ch-43) | 27,41,42 | Integrations、Marketplace、連携先公式 | Slack等との架空設計と公開実例を分ける。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 42 | [第44章 OrganizationとTeams](detailed-toc.md#ch-44) | 5,6,9 | Organizations、Teams、Roles | 5人チームのアクセス表を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 43 | [第16章 Issuesの高度な管理](detailed-toc.md#ch-16) | 15,44 | Issues、Organizations | 機能開発を分解し依存関係を設定する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 44 | [第20章 GitHub Projects](detailed-toc.md#ch-20) | 15,16 | Projects、GraphQL | 5人チームの計画と進捗ビューを作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 45 | [第45章 Organizationのポリシー](detailed-toc.md#ch-45) | 13,27,44 | Organizations policies、Security at scale | 例外申請を含む標準設定を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 46 | [第46章 GitHub Enterprise](detailed-toc.md#ch-46) | 6,44,45 | Enterprise admin、Onboarding、EMU | IdP接続を実行せず責任境界と障害対応を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 47 | [第47章 ガバナンス・監査・費用](detailed-toc.md#ch-47) | 8,32,45,46 | Audit logs、Billing、Secure at scale | 監査と予算の要件・測定・例外を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 48 | [第48章 OSS・コミュニティ・GitHubの周辺機能](detailed-toc.md#ch-48) | 9,15,18,21 | Community、Sponsors、Education、Support | OSS参加方針とsecret Gistの注意を説明する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 49 | [第49章 個人開発・小規模チームの実務運用](detailed-toc.md#ch-49) | 13,19,20,26,29,33,34,44 | 各機能Docs、企業公開事例 | 小規模アプリの開発運用を第三者が再現する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |
| 50 | [第50章 大規模開発・AI駆動開発の実務設計](detailed-toc.md#ch-50) | 32,35,39,43,47,49 | 各機能Docs、企業事例、外部公式 | 仕様根拠と仮定を分けアーキテクチャを審査する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。 |

## 章ごとの工程

1. Feature IDと不足出典を抽出。料金・権限・提供状態・UI条件を確認する。
2. 概念・選択基準・操作・比較・障害対応を執筆する。
3. 図・設定例・演習・理解度テスト・解答理由を作る。
4. 技術・出典・教育の3観点でレビューし、別の人が演習を再現する。
5. 台帳・リンク・ビルドを検証し、監査と進捗を更新してPRを作る。

単独章の完成でも全GitHubの網羅完了とは報告しない。
