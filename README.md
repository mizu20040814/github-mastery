# GitHub完全習得プロジェクト
GitHub.comを実務で活用するための日本語教材の調査・設計基盤。
仕様基準日2026-10-26。復元再調査日2026-11-14。本文は未執筆。

## 成果物
- [機能台帳](research/feature-inventory.csv) / [出典台帳](research/source-catalog.csv)
- [詳細目次](plans/detailed-toc.md) / [章対応](plans/feature-chapter-map.md)
- [調査範囲](research/SCOPE.md) / [品質基準](research/QUALITY_STANDARDS.md)
- [Docs分類](research/docs-taxonomy.md) / [UI Map](research/ui-map.md)
- [制作計画](plans/master-plan.md) / [進捗](plans/STATUS.md)
- [監査](audits/audit-report.md) / [残課題](research/research-gaps.md)

## 検証
```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python scripts/integrate_research.py
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build_site.py
```
生成物は.buildとsiteに保存。サイト公開は別承認。
概要verifiedは全仕様・プラン・権限確認済みの意味ではない。UIと実践の確認状態も別列で記録する。
前回環境の未push成果は消失したため、今回の台帳は再確認したデータで構成する。過去報告の290機能・183出典を復元済みの実績として流用しない。
