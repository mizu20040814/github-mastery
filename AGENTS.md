# 制作ルール
最初にREADME、plans/STATUS.md、audits/audit-report.mdとresearch/research-gaps.mdを読む。
対象GitHub.com、仕様基準2026-10-26。実際の確認日と公開日を区別。日付なし現行Docsから基準日当時の仕様を断定しない。
Phase0-2のみ。50章本文の大量生成は禁止。公式Docsを優先し、開いていないURLは確認済みにしない。UI、実践、概要、料金、権限、提供状態は独立管理。
research/fragments/*.jsonが原本。scripts/integrate_research.pyでCSVと章対応を生成し、validate.pyとbuild_site.pyを実行。
未確認は不明/未検証。全Docsの母集団未確定のため100%網羅を主張しない。廃止機能も履歴を残す。
独立した調査は共通プロトコルに従ってサブエージェント分担可能。
専用branchで小さくcommitし、途中でもpushして永続保存。mainへの初期化pushは過去自動承認レビューが拒否したため、明示承認なしに再試行しない。main merge/公開設定変更/有料契約/本番公開は承認が必要。
