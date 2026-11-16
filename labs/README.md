# Lab A〜Eの制作計画

更新2026-11-14。演習本文とサンプル実装はPhase 5で制作する。読者の操作・判断を中心にし、AI完全自動操作を前提にしない。

| Lab | 目的と対象 | 制作順 | 成果物と採点 | 前提・代替 |
|---|---|---|---|---|
| A 個人Webアプリ | Repository、Git、Issue、PR、Actions、Dependabot、Releases、Pages | 課題→branch→PR→CI→release→公開計画 | 履歴・PR・check・生成サイト・復旧説明 | 個人アカウントと使い捨てrepo。Pages公開は別承認。公開せずbuildまでで採点可能 |
| B 5人チーム | Org、Teams、Roles、Projects、CODEOWNERS、reviews、Rulesets、Merge Queue | 権限表→課題分解→レビュー→統合 | アクセス表・Project・承認拒否ケース・merge履歴 | 同意済み参加者とOrg。対応プランがなければqueueは状態遷移の設計演習 |
| C CI/CD・Security | workflows、tests、CodeQL、Dependabot、secret scanning、environments、承認、release automation | CI→脅威モデル→検出→承認配送 | YAML・成功/失敗証拠・alert対応・由来検証 | 使い捨て環境、機能条件を事前確認。本物の秘密値を使わず本番配送をしない |
| D AI開発 | Issueからタスク、AI変更、PR、AI review、修正、CI、人間承認 | 要求明確化→変更案→検証→承認 | 指示・diff・指摘評価・check・人間判断の理由 | Copilot/Codex/Claude等を別製品として比較。契約未確認なら架空設計と保存済みfixtureで演習 |
| E 大規模組織 | Enterprise、identity、policies、access、audit、標準CI/開発環境 | 要件→権限→継承→例外→監査・費用 | 構成図・責任表・policy表・障害対応・費用仮定 | 仕様調査と設計演習を分離。契約のないEnterprise実機成功を装わない |

## 各演習の必須構成

目的、前提章、Feature IDs、確認日、製品/版、plan/role/visibility、想定費用、作る対象、手順、各段階の期待結果、よくある失敗、検証、採点、片付け、出典を記載する。

実行証拠は日時・環境・コマンド・結果を記録し、秘密値・個人情報を除く。操作できない場合は「未実行の設計演習」と表示し、実機再現性とは別採点にする。

## 評価

機能の達成40%、選択理由20%、権限と安全境界20%、再現・復旧20%を基本に調整する。成功だけでなく、権限不足・check失敗・承認拒否・依存停止を観察し説明できるか評価する。別の読者が初期状態から再現してレビューする。

削除・権限変更・有料実行・公開は対象と許可を確認し、実行不要の代替を用意する。AIが生成したコードも人間がレビューし、最終承認を記録する。
