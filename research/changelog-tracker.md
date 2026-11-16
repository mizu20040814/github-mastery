# Changelogの確認と仕様更新

調査基準日: **2026-10-26**。復元再確認日: **2026-11-14**。

前回ファイルは環境再作成で失われたため、今回は再取得した出典と機能だけを台帳に登録した。過去の件数を今回の確認数へ流用しない。

## 継続調査の方法

1. [公式Changelog](https://github.blog/changelog/)を開き、前回確認日と1週間重なる日付範囲で新着・改善・廃止を確認する。RSSは発見用とし、履歴全体の分母にはしない。
2. タイトル・URLを候補登録し、記事本文を開いてからopenedへ変更する。検索抜粋だけでは確認済みとしない。
3. 公開日、適用日、GA/Preview/Deprecated/Retired、対象plan、権限、既定値、API版を分けて記録する。関連Docsを実際に開いて照合する。
4. 変更をFeature IDと章・演習・図へ対応づける。名称変更は旧名をnotesに残し、廃止行を削除しない。
5. DocsとChangelogの差は両方保存し、実UI・段階展開・更新時点を調べる。原因が不明なら未解消と記す。
6. 基準日後の記事や変更は「追補」に分ける。日付のない現行Docsを基準日の履歴版とみなさない。
7. 台帳統合、参照・リンク検証、strict buildを実行し、監査と引き継ぎを更新して専用ブランチへ保存する。

## 今回確認した変更

| 対象 | 根拠と確認範囲 | 基準日との関係 |
|---|---|---|
| Copilotのglobal default | [2026-10-22発表](https://github.blog/changelog/2026-10-22-global-default-for-copilot-features-generally-available/)。10/26までの段階展開、明示選択保持、Preview opt-inを確認 | 基準日以前の発表。個々の環境への適用はUI未検証 |
| GitHub Models | [現行Docs](https://docs.github.com/en/github-models)が2026-07-30完全終了を明示 | 終了日は基準日以前。Copilotとは別サービス |
| GitHub Spark on github.com | [2026-08-04発表](https://github.blog/changelog/2026-08-04-upcoming-deprecation-of-github-spark-on-github-com/)。新規停止・8/31までexport・既存deploy app継続・llm()停止を区別 | 基準日以前の発表。全appが停止すると説明しない |
| 新Copilot cloud体験 | [現行Docs](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github)が2026-10-28開始を明示 | **基準日後の追補**。旧Chat/cloud agentと混同しない |
| RepositoryのModerate role | [現行role表](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)に存在 | 導入日未確認。基準日のrole表へそのまま適用しない |

上表の確認済み出典はSRC-AIの台帳に記録している。2026年以前・全カテゴリのChangelog遡及照合は未完了である。

## 次回の差分記録

| 記事URL | 公開日 | 適用日 | Feature ID | 変更内容 | Docsとの整合 | 章・演習 | 対応状態 |
|---|---|---|---|---|---|---|---|
| 実際に開いたURL | YYYY-MM-DD | 日付/不明 | GH-… | 根拠付き要約 | 一致/差分未解消 | 章番号 | 候補/調査/修正/検証 |
