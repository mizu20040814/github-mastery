# 詳細目次と学習設計

基準日2026-10-26、復元日2026-11-14。12部50章を維持。教材本文ではなく、執筆前に調査する仕様書である。現行Docsの確認日と基準日を区別し、UI・プラン・権限・状態の未確認を解消してから手順を書く。

初期案から章を増やさず、issue fields、stacked PR、Findings、Agent Skills、MCP、AI承認、lockfiles等を既存節に含めた。新発見の状態は台帳を正とし、未検証候補は断定しない。

[制作計画](master-plan.md) / [制作順序](chapter-production-plan.md) / [機能対応](feature-chapter-map.md) / [演習](../labs/README.md)

## 第1部

<a id="ch-01"></a>

### 第1章 GitとGitHubの仕組み

**学習目標:** Gitの履歴モデルとリモート同期を説明できる

**前提:** プログラミングの基本操作

- 1.1 分散管理 — 1.1.1 GitとGitHub / 1.1.2 ローカルとremote
- 1.2 データ構造 — 1.2.1 blob・tree・commit / 1.2.2 参照・HEAD・index
- 1.3 履歴操作 — 1.3.1 fetch・pull・push / 1.3.2 revert・resetの判断

**演習:** A:小さなcommitと参照の移動を図示する

**出典調査軸:** Get started、Git公式

**レビュー:** 小さなcommitと参照の移動を図示する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-01)

<a id="ch-02"></a>

### 第2章 GitHub.comの全体構造

**学習目標:** 所有者と管理スコープを区別し必要な画面へ移動できる

**前提:** 第1章

- 2.1 管理境界 — 2.1.1 個人 / 2.1.2 Organization・Enterprise
- 2.2 全体導線 — 2.2.1 Dashboard・Feed / 2.2.2 検索・作成メニュー
- 2.3 製品境界 — 2.3.1 GitHub.comとGHES / 2.3.2 Desktop・Mobile・外部サービス

**演習:** A:公開閲覧とログイン時の導線を比較する

**出典調査軸:** Get started、Account、Repositories

**レビュー:** 公開閲覧とログイン時の導線を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-02)

<a id="ch-03"></a>

### 第3章 GitHubの検索機能

**学習目標:** 対象と構文を選び検索漏れを説明できる

**前提:** 第2章

- 3.1 一般検索 — 3.1.1 修飾子 / 3.1.2 並べ替え・絞込み
- 3.2 Code Search — 3.2.1 正規表現・symbol / 3.2.2 索引と既定branch
- 3.3 実務検索 — 3.3.1 保存検索 / 3.3.2 API検索との違い

**演習:** A:既知の対象を使いヒットと非ヒットを説明する

**出典調査軸:** Search、REST Search

**レビュー:** 既知の対象を使いヒットと非ヒットを説明する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-03)

<a id="ch-04"></a>

### 第4章 GitHubの画面操作と表示

**学習目標:** 表示設定とアクセシビリティを目的に合わせて使える

**前提:** 第2章

- 4.1 表示設定 — 4.1.1 Appearance / 4.1.2 日時・言語・幅
- 4.2 入力支援 — 4.2.1 ショートカット / 4.2.2 command palette
- 4.3 文章と操作 — 4.3.1 Markdown・添付 / 4.3.2 フォーカス・モバイル

**演習:** A:キーボードだけでIssueを探し表示差を記録する

**出典調査軸:** Account、Accessibility、Writing

**レビュー:** キーボードだけでIssueを探し表示差を記録する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-04)

## 第2部

<a id="ch-05"></a>

### 第5章 AccountとProfile

**学習目標:** 個人情報の公開範囲とアカウント運用を設計できる

**前提:** 第2章

- 5.1 公開プロフィール — 5.1.1 README・pin / 5.1.2 Contributions・Achievements
- 5.2 識別情報 — 5.2.1 username・email / 5.2.2 公開とprivate activity
- 5.3 ライフサイクル — 5.3.1 rename・export / 5.3.2 閉鎖・継承

**演習:** A:本人と公開閲覧のプロフィールを比較する

**出典調査軸:** Account and profile

**レビュー:** 本人と公開閲覧のプロフィールを比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-05)

<a id="ch-06"></a>

### 第6章 認証とアカウント保護

**学習目標:** 認証手段と復旧・失効を適切に設計できる

**前提:** 第1章、第5章

- 6.1 ログイン保護 — 6.1.1 2FA・passkeys / 6.1.2 recovery codes
- 6.2 Git認証 — 6.2.1 HTTPS・credential helper / 6.2.2 SSH・署名鍵
- 6.3 認証資源 — 6.3.1 PAT・Appsの選択 / 6.3.2 session・security log

**演習:** A:読取専用認証と失効時の動作を確認する

**出典調査軸:** Authentication、Apps

**レビュー:** 読取専用認証と失効時の動作を確認する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-06)

<a id="ch-07"></a>

### 第7章 NotificationsとSubscriptions

**学習目標:** 通知原因と受信経路を制御できる

**前提:** 第2章、第5章

- 7.1 通知モデル — 7.1.1 reason・参加 / 7.1.2 Watchとsubscription
- 7.2 受信処理 — 7.2.1 Inbox・saved filters / 7.2.2 done・unsubscribe
- 7.3 配信設計 — 7.3.1 メールとWeb / 7.3.2 チームの通知負荷

**演習:** B:レビュー依頼とmentionの通知を比較する

**出典調査軸:** Subscriptions and notifications

**レビュー:** レビュー依頼とmentionの通知を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-07)

<a id="ch-08"></a>

### 第8章 Billingと利用プラン

**学習目標:** 機能条件と従量費用を分けて判断できる

**前提:** 第5章

- 8.1 プラン — 8.1.1 Free・Pro / 8.1.2 Team・Enterprise
- 8.2 利用量 — 8.2.1 Actions・storage / 8.2.2 Codespaces・AI
- 8.3 費用統制 — 8.3.1 budget・alerts / 8.3.2 請求役割・cost center

**演習:** A:無料枠と従量項目を出典日付きで試算する

**出典調査軸:** Billing、Plans

**レビュー:** 無料枠と従量項目を出典日付きで試算する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-08)

## 第3部

<a id="ch-09"></a>

### 第9章 Repositoryの作成と管理

**学習目標:** 所有者と可視性に応じてRepositoryを管理できる

**前提:** 第1章、第6章

- 9.1 作成 — 9.1.1 空repo・template / 9.1.2 public・private・internal
- 9.2 派生と移行 — 9.2.1 fork・duplicate / 9.2.2 import・transfer
- 9.3 ライフサイクル — 9.3.1 archive / 9.3.2 delete・restoreの条件

**演習:** A:使い捨てRepositoryを作り所有と可視性を説明する

**出典調査軸:** Repositories、Migrations

**レビュー:** 使い捨てRepositoryを作り所有と可視性を説明する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-09)

<a id="ch-10"></a>

### 第10章 Codeタブの全機能

**学習目標:** コード閲覧と編集の導線を使い分けられる

**前提:** 第1章、第9章

- 10.1 閲覧 — 10.1.1 file tree・Go to file / 10.1.2 README・About
- 10.2 履歴追跡 — 10.2.1 history・blame / 10.2.2 permalink・diff
- 10.3 変更と取得 — 10.3.1 Web edit・upload / 10.3.2 clone・download・web editor

**演習:** A:固定commitのpermalinkと変更PRを作成する

**出典調査軸:** Repositories、Code navigation

**レビュー:** 固定commitのpermalinkと変更PRを作成する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-10)

<a id="ch-11"></a>

### 第11章 ブランチ・コミット管理

**学習目標:** 履歴と参照を安全に扱い変更を追跡できる

**前提:** 第1章、第9章、第10章

- 11.1 参照管理 — 11.1.1 branches / 11.1.2 tags・default branch
- 11.2 コミット — 11.2.1 比較・署名 / 11.2.2 著者とcommitter
- 11.3 履歴設計 — 11.3.1 rebase・cherry-pick / 11.3.2 復旧と共有済み履歴

**演習:** A:作業branchとtagを作り差分を検証する

**出典調査軸:** Repositories、Authentication、Git

**レビュー:** 作業branchとtagを作り差分を検証する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-11)

<a id="ch-12"></a>

### 第12章 RepositoryのSettings

**学習目標:** 設定の影響範囲と変更権限を把握できる

**前提:** 第8章、第9章

- 12.1 General — 12.1.1 機能toggle / 12.1.2 PRとmerge設定
- 12.2 アクセス — 12.2.1 collaborators・teams / 12.2.2 deploy keys・Apps
- 12.3 開発設定 — 12.3.1 Actions・secrets / 12.3.2 environments・Pages

**演習:** A:readとadminで設定の見え方を比較する

**出典調査軸:** Repositories、Actions、Organizations

**レビュー:** readとadminで設定の見え方を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-12)

<a id="ch-13"></a>

### 第13章 Rulesetsとブランチ保護

**学習目標:** 複数の保護ルールとbypassを設計できる

**前提:** 第11章、第12章

- 13.1 保護モデル — 13.1.1 branch protection / 13.1.2 rulesetsの重なり
- 13.2 要件 — 13.2.1 reviews・checks / 13.2.2 署名・履歴・push制約
- 13.3 bypassと評価 — 13.3.1 役割と例外 / 13.3.2 evaluate・insights

**演習:** B:承認とcheckの成功・拒否ケースを設計する

**出典調査軸:** Rulesets、Protected branches

**レビュー:** 承認とcheckの成功・拒否ケースを設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-13)

<a id="ch-14"></a>

### 第14章 InsightsとRepository分析

**学習目標:** 集計の制約を踏まえてRepositoryを評価できる

**前提:** 第9章、第15章、第17章

- 14.1 活動 — 14.1.1 Pulse・contributors / 14.1.2 commits・code frequency
- 14.2 流入と関係 — 14.2.1 Traffic / 14.2.2 network・forks
- 14.3 品質と運用 — 14.3.1 dependency graph / 14.3.2 community・集計遅延

**演習:** B:観測期間と権限を固定した分析を作る

**出典調査軸:** Repositories Insights、Community

**レビュー:** 観測期間と権限を固定した分析を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-14)

## 第4部

<a id="ch-15"></a>

### 第15章 GitHub Issues

**学習目標:** 再現可能なIssueとトリアージ手順を作れる

**前提:** 第3章、第9章

- 15.1 作成 — 15.1.1 templates・forms / 15.1.2 再現条件・添付
- 15.2 整理 — 15.2.1 labels・milestones / 15.2.2 assignee・検索
- 15.3 ライフサイクル — 15.3.1 close reason / 15.3.2 transfer・lock・archive相違

**演習:** A:不具合テンプレートから課題を登録する

**出典調査軸:** Issues、Issue forms

**レビュー:** 不具合テンプレートから課題を登録する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-15)

<a id="ch-16"></a>

### 第16章 Issuesの高度な管理

**学習目標:** 階層・依存・組織メタデータを使い分けられる

**前提:** 第15章、第44章

- 16.1 構造化 — 16.1.1 sub-issues / 16.1.2 依存とblocked
- 16.2 共通分類 — 16.2.1 issue types / 16.2.2 issue fieldsとlabels
- 16.3 運用 — 16.3.1 triage・横断検索 / 16.3.2 移動・旧tasklistとの違い

**演習:** B:機能開発を分解し依存関係を設定する

**出典調査軸:** Issues、Organizations

**レビュー:** 機能開発を分解し依存関係を設定する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-16)

<a id="ch-17"></a>

### 第17章 Pull Requestの全体像

**学習目標:** baseとheadを理解しレビュー可能なPRを作れる

**前提:** 第11章、第15章

- 17.1 作成 — 17.1.1 compare・fork / 17.1.2 Draftとready
- 17.2 構成 — 17.2.1 Conversation・Commits / 17.2.2 Checks・Files changed・Findings
- 17.3 関連付け — 17.3.1 Issue closing / 17.3.2 stacked PRの単位

**演習:** A:IssueからDraft PRを作りレビュー準備をする

**出典調査軸:** Pull requests、Issues

**レビュー:** IssueからDraft PRを作りレビュー準備をする。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-17)

<a id="ch-18"></a>

### 第18章 Code Reviewの完全解説

**学習目標:** レビュー権限と承認要件を運用できる

**前提:** 第13章、第17章

- 18.1 レビュー操作 — 18.1.1 comments・suggestions / 18.1.2 approve・request changes
- 18.2 所有と統制 — 18.2.1 CODEOWNERS / 18.2.2 required reviews・stale approval
- 18.3 運用 — 18.3.1 差分の読み方 / 18.3.2 dismiss・再レビュー

**演習:** B:担当所有者のレビューと修正を循環させる

**出典調査軸:** Pull requests reviews、CODEOWNERS

**レビュー:** 担当所有者のレビューと修正を循環させる。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-18)

<a id="ch-19"></a>

### 第19章 PRのマージと変更履歴

**学習目標:** マージ方式とqueueを選び履歴を保守できる

**前提:** 第13章、第18章、第22章

- 19.1 マージ方式 — 19.1.1 merge commit / 19.1.2 squash・rebase
- 19.2 保護との協調 — 19.2.1 required checks / 19.2.2 auto-merge・merge queue
- 19.3 変更後 — 19.3.1 branch削除 / 19.3.2 revert・stackの再整列

**演習:** B:同じ変更を各方式で統合し履歴を比較する

**出典調査軸:** Pull requests、Merge queue、Actions

**レビュー:** 同じ変更を各方式で統合し履歴を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-19)

<a id="ch-20"></a>

### 第20章 GitHub Projects

**学習目標:** 課題を複数ビューと自動化で管理できる

**前提:** 第15章、第16章

- 20.1 データ — 20.1.1 items・drafts / 20.1.2 custom fields・iteration
- 20.2 ビュー — 20.2.1 table・board / 20.2.2 roadmap・group・filter
- 20.3 運用 — 20.3.1 workflows・templates / 20.3.2 insights・access・API

**演習:** B:5人チームの計画と進捗ビューを作る

**出典調査軸:** Projects、GraphQL

**レビュー:** 5人チームの計画と進捗ビューを作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-20)

<a id="ch-21"></a>

### 第21章 Discussionsと共同作業

**学習目標:** 課題追跡と会話・知識共有を分けて運用できる

**前提:** 第9章、第15章、第17章

- 21.1 Discussions — 21.1.1 categories・forms / 21.1.2 回答・polls・moderation
- 21.2 知識 — 21.2.1 Wiki・sidebar / 21.2.2 history・アクセス
- 21.3 共同作業 — 21.3.1 Issueとの転換 / 21.3.2 community標準文書

**演習:** B:質問から回答とWiki記録へつなぐ

**出典調査軸:** Discussions、Wiki、Community

**レビュー:** 質問から回答とWiki記録へつなぐ。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-21)

## 第5部

<a id="ch-22"></a>

### 第22章 GitHub Actionsの基本

**学習目標:** イベントからjobとcheckまでの流れを説明できる

**前提:** 第9章、第11章、第17章

- 22.1 モデル — 22.1.1 workflow・event / 22.1.2 job・step・action
- 22.2 初回CI — 22.2.1 checkout・setup / 22.2.2 test・失敗結果
- 22.3 観察 — 22.3.1 run・logs / 22.3.2 artifacts・再実行

**演習:** A:成功と失敗するテストCIを作る

**出典調査軸:** Actions quickstart、Concepts

**レビュー:** 成功と失敗するテストCIを作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-22)

<a id="ch-23"></a>

### 第23章 Workflowの詳細仕様

**学習目標:** YAMLと実行コンテキストを正しく設計できる

**前提:** 第22章

- 23.1 トリガー — 23.1.1 events・filters / 23.1.2 ref・SHAの違い
- 23.2 データ — 23.2.1 expressions・contexts / 23.2.2 env・outputs・needs
- 23.3 実行制御 — 23.3.1 matrix・conditions / 23.3.2 concurrency・timeout

**演習:** C:イベントごとのrefとtoken条件を比較する

**出典調査軸:** Workflow syntax、Events、Contexts

**レビュー:** イベントごとのrefとtoken条件を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-23)

<a id="ch-24"></a>

### 第24章 Actionsの高度な設計

**学習目標:** 再利用・性能・保守性を両立できる

**前提:** 第23章

- 24.1 再利用 — 24.1.1 reusable workflows / 24.1.2 composite・JS・Docker actions
- 24.2 成果物 — 24.2.1 artifacts / 24.2.2 cache key・restore
- 24.3 並列と依存 — 24.3.1 matrix・fan-out / 24.3.2 service containers・lockfiles

**演習:** C:cache有無の同等性と再利用境界を確認する

**出典調査軸:** Actions reuse、Cache、Artifacts

**レビュー:** cache有無の同等性と再利用境界を確認する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-24)

<a id="ch-25"></a>

### 第25章 Runnerと実行環境

**学習目標:** 隔離と容量に応じてRunnerを選べる

**前提:** 第23章、第27章

- 25.1 実行方式 — 25.1.1 hosted・larger / 25.1.2 self-hosted・ephemeral
- 25.2 組織管理 — 25.2.1 groups・labels / 25.2.2 ARC・network
- 25.3 保守 — 25.3.1 images・updates / 25.3.2 limits・metrics・残存状態

**演習:** C:信頼境界と実行環境の比較表を設計する

**出典調査軸:** Actions runners、ARC

**レビュー:** 信頼境界と実行環境の比較表を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-25)

<a id="ch-26"></a>

### 第26章 CDとデプロイ

**学習目標:** 承認・環境・認証を含む配布を設計できる

**前提:** 第23章、第27章

- 26.1 環境 — 26.1.1 environments・variables / 26.1.2 secrets・branch制約
- 26.2 承認 — 26.2.1 reviewers・wait / 26.2.2 自己承認・保護ルール
- 26.3 配送 — 26.3.1 deployments・OIDC / 26.3.2 rollback・release連携

**演習:** C:本番公開せず承認付き配送の状態遷移を作る

**出典調査軸:** Environments、Deployments、OIDC

**レビュー:** 本番公開せず承認付き配送の状態遷移を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-26)

<a id="ch-27"></a>

### 第27章 Actionsのセキュリティ

**学習目標:** 外部入力とtokenの境界を守れる

**前提:** 第6章、第23章

- 27.1 脅威 — 27.1.1 untrusted PR / 27.1.2 script injection・checkout対象
- 27.2 認証 — 27.2.1 permissions・GITHUB_TOKEN / 27.2.2 secrets・OIDC
- 27.3 供給元 — 27.3.1 SHA pin・lockfile / 27.3.2 fork承認・runner隔離

**演習:** C:秘密値なしの入力で境界を検証する

**出典調査軸:** Actions security、OIDC

**レビュー:** 秘密値なしの入力で境界を検証する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-27)

## 第6部

<a id="ch-28"></a>

### 第28章 Securityタブの全体構造

**学習目標:** 検出・修正・統制機能と利用条件を分類できる

**前提:** 第8章、第12章

- 28.1 製品と画面 — 28.1.1 Code Security / 28.1.2 Secret Protection・Quality
- 28.2 運用 — 28.2.1 alerts・roles / 28.2.2 security policy・advisories
- 28.3 組織連携 — 28.3.1 overview・configurations / 28.3.2 plan・visibility条件

**演習:** C:検出機能と契約・権限の表を作る

**出典調査軸:** Security and quality、Billing

**レビュー:** 検出機能と契約・権限の表を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-28)

<a id="ch-29"></a>

### 第29章 Dependabotと依存関係

**学習目標:** 更新・脆弱性・導入差分を分けて管理できる

**前提:** 第22章、第28章

- 29.1 把握 — 29.1.1 dependency graph / 29.1.2 SBOM・manifest・lockfile
- 29.2 検出と更新 — 29.2.1 alerts・security updates / 29.2.2 version updates・groups
- 29.3 統制 — 29.3.1 dependency review / 29.3.2 private registry・auto-triage

**演習:** C:更新PRと導入差分検査を比較する

**出典調査軸:** Supply chain、Dependabot

**レビュー:** 更新PRと導入差分検査を比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-29)

<a id="ch-30"></a>

### 第30章 Code Security

**学習目標:** 解析範囲と修正支援の限界を説明できる

**前提:** 第23章、第28章

- 30.1 解析 — 30.1.1 code scanning・CodeQL / 30.1.2 default・advanced setup
- 30.2 連携 — 30.2.1 SARIF・言語build / 30.2.2 query packs・schedule
- 30.3 修正と品質 — 30.3.1 Autofix・AI Scan / 30.3.2 triage・quality・課金

**演習:** C:検証用コードで検出と修正結果を照合する

**出典調査軸:** Code scanning、CodeQL、Quality

**レビュー:** 検証用コードで検出と修正結果を照合する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-30)

<a id="ch-31"></a>

### 第31章 Secret Security

**学習目標:** 漏えい検出と失効・再発防止を運用できる

**前提:** 第6章、第28章

- 31.1 検出 — 31.1.1 secret scanning / 31.1.2 patterns・validity
- 31.2 予防 — 31.2.1 push protection / 31.2.2 bypass・delegated review
- 31.3 事故対応 — 31.3.1 revoke・rotate / 31.3.2 history除去と監査

**演習:** C:本物の秘密値を使わず対応手順を設計する

**出典調査軸:** Secret scanning、Push protection

**レビュー:** 本物の秘密値を使わず対応手順を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-31)

<a id="ch-32"></a>

### 第32章 サプライチェーンと品質統制

**学習目標:** 成果物の由来と依存ポリシーを検証できる

**前提:** 第13章、第24章、第29章、第30章、第31章

- 32.1 証跡 — 32.1.1 artifact attestations / 32.1.2 provenance・SBOM
- 32.2 依存統制 — 32.2.1 license・malware / 32.2.2 package firewall・exceptions
- 32.3 統合 — 32.3.1 rulesets・checks / 32.3.2 issuer・subject・digest

**演習:** C:署名有無と検証条件成立の違いを評価する

**出典調査軸:** Supply chain、Attestations、Rulesets

**レビュー:** 署名有無と検証条件成立の違いを評価する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-32)

## 第7部

<a id="ch-33"></a>

### 第33章 Releases・Packages・Registry

**学習目標:** 配布物の版・公開範囲・権限を管理できる

**前提:** 第11章、第24章、第32章

- 33.1 Releases — 33.1.1 tags・notes / 33.1.2 assets・immutable releases
- 33.2 Packages — 33.2.1 registry種別 / 33.2.2 GHCR・認証
- 33.3 運用 — 33.3.1 権限継承・削除復元 / 33.3.2 retention・費用

**演習:** A:未公開のrelease案と配布物digestを作る

**出典調査軸:** Releases、Packages、GHCR

**レビュー:** 未公開のrelease案と配布物digestを作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-33)

<a id="ch-34"></a>

### 第34章 GitHub Pages

**学習目標:** ビルドと公開・ドメイン設定を分けて設計できる

**前提:** 第8章、第22章、第26章

- 34.1 生成 — 34.1.1 branch source / 34.1.2 Actions・static assets
- 34.2 公開 — 34.2.1 domain・HTTPS / 34.2.2 access・visibility
- 34.3 制約 — 34.3.1 limits・cache / 34.3.2 404・path・公開承認

**演習:** A:ローカル相当の生成サイトを検証し公開手順を記す

**出典調査軸:** Pages、Actions deployment

**レビュー:** ローカル相当の生成サイトを検証し公開手順を記す。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-34)

<a id="ch-35"></a>

### 第35章 GitHub Codespaces

**学習目標:** 再現可能な開発環境と費用境界を設計できる

**前提:** 第8章、第9章、第25章

- 35.1 環境定義 — 35.1.1 devcontainer / 35.1.2 features・prebuilds
- 35.2 利用 — 35.2.1 ports・secrets / 35.2.2 branch・resume・rebuild
- 35.3 統制 — 35.3.1 policy・machine / 35.3.2 timeout・retention・費用

**演習:** C:設定ファイルと実環境の確認項目を分ける

**出典調査軸:** Codespaces、Dev Containers、Billing

**レビュー:** 設定ファイルと実環境の確認項目を分ける。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-35)

## 第8部

<a id="ch-36"></a>

### 第36章 GitHub.com上のCopilot

**学習目標:** 支援対象とプラン・データ境界を説明できる

**前提:** 第6章、第8章、第10章

- 36.1 支援面 — 36.1.1 Chat・search / 36.1.2 code説明・モデル選択
- 36.2 契約 — 36.2.1 plans・usage / 36.2.2 AI credits・管理policy
- 36.3 信頼 — 36.3.1 出典・検証 / 36.3.2 data use・content exclusion

**演習:** D:回答の根拠と人間の検証手順を記録する

**出典調査軸:** Copilot、Plans、Changelog

**レビュー:** 回答の根拠と人間の検証手順を記録する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-36)

<a id="ch-37"></a>

### 第37章 Copilot Cloud Agent

**学習目標:** タスク割当からPRまでを承認付きで運用できる

**前提:** 第17章、第22章、第27章、第36章

- 37.1 タスク — 37.1.1 Issue・session / 37.1.2 指示・対象repo
- 37.2 実行 — 37.2.1 setup workflow / 37.2.2 firewall・secrets・permissions
- 37.3 変更 — 37.3.1 PR・review・修正 / 37.3.2 停止・費用・audit

**演習:** D:小さなIssueに対する変更案を人間が評価する

**出典調査軸:** Cloud agent、Sessions、Actions

**レビュー:** 小さなIssueに対する変更案を人間が評価する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-37)

<a id="ch-38"></a>

### 第38章 Copilot Code Review

**学習目標:** AI指摘と承認条件を区別できる

**前提:** 第18章、第36章

- 38.1 依頼 — 38.1.1 手動・自動 / 38.1.2 対象差分・設定
- 38.2 結果 — 38.2.1 comments・findings / 38.2.2 fix提案・再レビュー
- 38.3 統制 — 38.3.1 custom instructions / 38.3.2 プラン・AI承認・Preview

**演習:** D:AIが指摘しない問題も含めレビューを採点する

**出典調査軸:** Copilot code review、PR reviews

**レビュー:** AIが指摘しない問題も含めレビューを採点する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-38)

<a id="ch-39"></a>

### 第39章 AIエージェント連携と統制

**学習目標:** GitHub機能と外部ツールの権限境界を設計できる

**前提:** 第27章、第37章、第38章、第42章

- 39.1 文脈 — 39.1.1 custom instructions / 39.1.2 custom agents・skills
- 39.2 接続 — 39.2.1 MCP・tools / 39.2.2 hooks・prompt injection
- 39.3 運用 — 39.3.1 Codex・Claude等 / 39.3.2 承認・監査・人間の最終判断

**演習:** D:IssueからCI・人間承認までの責任分担を設計する

**出典調査軸:** Copilot customization、MCP、各ベンダー公式

**レビュー:** IssueからCI・人間承認までの責任分担を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-39)

## 第9部

<a id="ch-40"></a>

### 第40章 GitHub CLIと周辺ツール

**学習目標:** WebとCLIを使い分け結果を照合できる

**前提:** 第1章、第6章、第17章

- 40.1 CLI — 40.1.1 auth・repo・issue / 40.1.2 pr・workflow・release
- 40.2 拡張 — 40.2.1 gh api・pagination / 40.2.2 extensions・aliases
- 40.3 周辺 — 40.3.1 Desktop・Mobile / 40.3.2 Webとの差とOS制約

**演習:** A:同じPRをWebと読取CLIで比較する

**出典調査軸:** CLI manual、Desktop、Mobile

**レビュー:** 同じPRをWebと読取CLIで比較する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-40)

<a id="ch-41"></a>

### 第41章 GitHub API

**学習目標:** 認証・ページング・制限を扱う連携を設計できる

**前提:** 第6章、第15章、第17章、第40章

- 41.1 REST — 41.1.1 resources・version / 41.1.2 headers・conditional requests
- 41.2 GraphQL — 41.2.1 schema・query / 41.2.2 mutation・cost
- 41.3 堅牢性 — 41.3.1 pagination・retry / 41.3.2 secondary limits・権限不足

**演習:** C:読取APIの複数ページと失敗応答を処理する

**出典調査軸:** REST、GraphQL、Authentication

**レビュー:** 読取APIの複数ページと失敗応答を処理する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-41)

<a id="ch-42"></a>

### 第42章 GitHub AppsとWebhooks

**学習目標:** installation単位の権限とイベント処理を設計できる

**前提:** 第6章、第41章

- 42.1 認証方式 — 42.1.1 GitHub App / 42.1.2 OAuth App・PAT比較
- 42.2 App管理 — 42.2.1 registration・installation / 42.2.2 token・callback・permissions
- 42.3 Webhooks — 42.3.1 署名・payload / 42.3.2 redelivery・重複・順序

**演習:** C:fixtureで署名と冪等処理を検証する

**出典調査軸:** Apps、Webhooks、OAuth

**レビュー:** fixtureで署名と冪等処理を検証する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-42)

<a id="ch-43"></a>

### 第43章 外部サービス連携

**学習目標:** 連携目的と最小権限に応じて方式を選べる

**前提:** 第27章、第41章、第42章

- 43.1 連携方式 — 43.1.1 Marketplace / 43.1.2 Apps・API・webhooks
- 43.2 実務接続 — 43.2.1 chat・ticket / 43.2.2 CI・cloud・OIDC
- 43.3 保守 — 43.3.1 secret rotation / 43.3.2 障害・監査・解約

**演習:** B:Slack等との架空設計と公開実例を分ける

**出典調査軸:** Integrations、Marketplace、連携先公式

**レビュー:** Slack等との架空設計と公開実例を分ける。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-43)

## 第10部

<a id="ch-44"></a>

### 第44章 OrganizationとTeams

**学習目標:** メンバーとチームの権限を最小化できる

**前提:** 第5章、第6章、第9章

- 44.1 構成 — 44.1.1 members・outside collaborators / 44.1.2 teams・nested teams
- 44.2 権限 — 44.2.1 repo roles / 44.2.2 custom roles・権限の加算
- 44.3 運用 — 44.3.1 招待・offboarding / 44.3.2 owner・maintainer・可視性

**演習:** B:5人チームのアクセス表を作る

**出典調査軸:** Organizations、Teams、Roles

**レビュー:** 5人チームのアクセス表を作る。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-44)

<a id="ch-45"></a>

### 第45章 Organizationのポリシー

**学習目標:** 既定値と強制ポリシーの継承を説明できる

**前提:** 第13章、第27章、第44章

- 45.1 Repository — 45.1.1 defaults・creation / 45.1.2 rulesets・custom properties
- 45.2 アクセス — 45.2.1 2FA・SSO・IP / 45.2.2 Apps・OAuth・token policy
- 45.3 開発統制 — 45.3.1 Actions・runners / 45.3.2 Codespaces・Copilot・security configs

**演習:** E:例外申請を含む標準設定を設計する

**出典調査軸:** Organizations policies、Security at scale

**レビュー:** 例外申請を含む標準設定を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-45)

<a id="ch-46"></a>

### 第46章 GitHub Enterprise

**学習目標:** 企業IDと製品境界を踏まえて構成できる

**前提:** 第6章、第44章、第45章

- 46.1 製品 — 46.1.1 Cloud・Server / 46.1.2 GHE.com・data residency
- 46.2 Identity — 46.2.1 SAML・SCIM / 46.2.2 EMU・team sync・recovery
- 46.3 運用 — 46.3.1 organizations・teams / 46.3.2 migration・license・policy継承

**演習:** E:IdP接続を実行せず責任境界と障害対応を設計する

**出典調査軸:** Enterprise admin、Onboarding、EMU

**レビュー:** IdP接続を実行せず責任境界と障害対応を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-46)

<a id="ch-47"></a>

### 第47章 ガバナンス・監査・費用

**学習目標:** 監査証跡と費用統制の限界を説明できる

**前提:** 第8章、第32章、第45章、第46章

- 47.1 監査 — 47.1.1 audit log・API / 47.1.2 streaming・retention・イベント範囲
- 47.2 組織統制 — 47.2.1 security overview / 47.2.2 例外・委任・アクセス棚卸し
- 47.3 費用 — 47.3.1 licenses・usage / 47.3.2 cost center・budget・配賦

**演習:** E:監査と予算の要件・測定・例外を設計する

**出典調査軸:** Audit logs、Billing、Secure at scale

**レビュー:** 監査と予算の要件・測定・例外を設計する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-47)

## 第11部

<a id="ch-48"></a>

### 第48章 OSS・コミュニティ・GitHubの周辺機能

**学習目標:** 参加規範と支援制度を適切に利用できる

**前提:** 第9章、第15章、第18章、第21章

- 48.1 参加 — 48.1.1 community standards / 48.1.2 CONTRIBUTING・license・moderation
- 48.2 支援 — 48.2.1 Sponsors・Education / 48.2.2 Nonprofits・Skills / 48.2.3 Learn
- 48.3 周辺 — 48.3.1 Gistの公開性 / 48.3.2 Support・Status・制度の資格

**演習:** A:OSS参加方針とsecret Gistの注意を説明する

**出典調査軸:** Community、Sponsors、Education、Support

**レビュー:** OSS参加方針とsecret Gistの注意を説明する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-48)

## 第12部

<a id="ch-49"></a>

### 第49章 個人開発・小規模チームの実務運用

**学習目標:** 複数機能を一貫した小規模開発へ統合できる

**前提:** 第13章、第19章、第20章、第26章、第29章、第33章、第34章、第44章

- 49.1 起点 — 49.1.1 要求・Issue・Projects / 49.1.2 branch・PR・review
- 49.2 自動化 — 49.2.1 tests・Dependabot / 49.2.2 release・配送
- 49.3 保守 — 49.3.1 通知・権限・費用 / 49.3.2 障害復旧・改善

**演習:** A+B+C:小規模アプリの開発運用を第三者が再現する

**出典調査軸:** 各機能Docs、企業公開事例

**レビュー:** 小規模アプリの開発運用を第三者が再現する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-49)

<a id="ch-50"></a>

### 第50章 大規模開発・AI駆動開発の実務設計

**学習目標:** 統制と開発体験を両立する設計を評価できる

**前提:** 第32章、第35章、第39章、第43章、第47章、第49章

- 50.1 基盤 — 50.1.1 Enterprise・identity / 50.1.2 標準CI・開発環境
- 50.2 AI運用 — 50.2.1 agent・MCP・review / 50.2.2 人間承認・監査
- 50.3 評価 — 50.3.1 security・費用・生産性 / 50.3.2 例外・移行・残余リスク

**演習:** D+E:仕様根拠と仮定を分けアーキテクチャを審査する

**出典調査軸:** 各機能Docs、企業事例、外部公式

**レビュー:** 仕様根拠と仮定を分けアーキテクチャを審査する。期待結果・失敗結果・権限/プラン条件を出典と照合し、未実施部分を区別する。

**対応機能:** [章別対応表](feature-chapter-map.md#ch-50)
