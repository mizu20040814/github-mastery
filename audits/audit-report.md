# Phase0-2監査
仕様基準2026-10-26、復元再確認2026-11-14。
前回環境の未push成果消失により調査基盤を復元した。過去報告の数値や検証結果を再現済みとして流用しない。
調査対象はGitHub.com。選定した公式Docsの入口/下位ページを分類し、機能/出典/章の対応を記録する。全Docsの母集団は未確定で、全体網羅率は算出しない。
登録機能数はfeature-inventory.csv行数、出典数はsource-catalog.csv行数。本文確認数はverification_status=openedの一意URL数。詳細は[集計](metrics.json)。
認証付きGitHub UIと実践演習は未検証。Docsから整理したUI Mapを実機検証済みとして扱わない。プラン/権限/GAの不明は台帳へ明示する。
機械検証は[結果](validation-results.json)、サイトは[ビルド検証](site-build.md)を参照。全出典の主張レベル独立監査と名称違いの意味重複監査は未完了。
[残課題](../research/research-gaps.md)を章ごとに解消してから本文制作へ進む。Enterprise実機不可の場合は設計演習へ分離する。
main向けPRは比較元mainが存在しないため保留。main初期化pushは自動承認レビューが明示承認不足を理由に拒否した。専用branch保存を継続する。
