# Phase0-2監査
仕様基準2026-10-26、復元再確認2026-11-14。
前回環境の未push成果消失により調査基盤を復元した。過去報告の数値や検証結果を再現済みとして流用しない。
調査対象はGitHub.com。選定した公式Docsの入口/下位ページを分類し、機能/出典/章の対応を記録する。全Docsの母集団は未確定で、全体網羅率は算出しない。
登録機能数はfeature-inventory.csv行数、出典数はsource-catalog.csv行数。本文確認数はverification_status=openedの一意URL数。詳細は[集計](metrics.json)。
認証付きGitHub UIと実践演習は未検証。Docsから整理したUI Mapを実機検証済みとして扱わない。プラン/権限/GAの不明は台帳へ明示する。
機械検証は[結果](validation-results.json)、サイトは[ビルド検証](site-build.md)を参照。全出典の主張レベル独立監査と名称違いの意味重複監査は未完了。
[残課題](../research/research-gaps.md)を章ごとに解消してから本文制作へ進む。Enterprise実機不可の場合は設計演習へ分離する。
main向けPRは比較元mainが存在しないため保留。main初期化pushは自動承認レビューが明示承認不足を理由に拒否した。専用branch保存を継続する。

## 今回の集計
234機能、99一意出典URL（91本文確認、8取得不可）。本文確認Docsは88一意URL。登録機能の概要は234件照合、UI/実践は0/234件確認。27分類、12部50章。母集団は今回登録した台帳であり、全GitHubの網羅率ではない。
第12・28章は総覧として関連機能を再利用、第49・50章は総合演習として再利用する。全50章の独立機能を水増ししていない。
登録ID/URL/同一機能名の完全一致重複は検査済み。名称の異なる意味重複は追加レビューが必要。プラン・権限・GA/Previewには不明が残る。

## 最終技術検証
MkDocs strict buildは警告0で成功。CSV/ID/出典/章参照/内部リンク検証成功。日本語検索・Mermaid描画・1440px表示・390pxメニューの4項目はChromiumで成功し、通信失敗/JavaScriptエラー0。pip checkとPython構文も成功。
GitHub Actionsの[実行43575438955](https://github.com/mizu20040814/github-mastery/actions/runs/43575438955)はcommit e16d15fでsuccessを確認。途中保存の不完全な構成で発生した先行run失敗は統合後に解消した。
公開は未実施。成果物はcodex/phase-0-2-foundationへpush済み。main比較元の作成は承認待ち。
