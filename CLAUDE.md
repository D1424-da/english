# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## プロジェクト概要

**English Diagnosis** — 日本の中高生（中1〜高3）向け英語学習診断アプリ。
20問の診断で弱点単元を特定し、単元ごとの具体的な勉強法と演習問題で克服を支援する。
利用者はスマートフォン中心の学生。UIはすべて日本語。

## 技術スタック

- **Backend**: Python 3.11 + FastAPI + SQLAlchemy（`backend/`）
- **Frontend**: React 19 + Vite（`frontend/`）。SPAだが react-router は不使用 — `App.jsx` の `page` state による画面切り替え
- **DB**: 開発 = SQLite（`backend/english_app.db`）、本番 = Supabase PostgreSQL（無料枠、Transaction Pooler 経由）
- **デプロイ**: Render 無料枠（Docker）。**mainブランチへのpushで自動デプロイ**
- 認証は bcrypt によるパスワードハッシュのみ（JWTなし、フロントは localStorage に userId を保存）

## よく使うコマンド

```bash
# バックエンド起動（開発）
cd backend && python -c "import uvicorn; uvicorn.run('main:app', host='0.0.0.0', port=8000)"

# シード投入（冪等・既存データは消さない）
cd backend && python -m seed.seed_data   # 全シード＋データ修正マイグレーションを連鎖実行

# フロントエンドビルド（バックエンドが frontend/dist を配信する）
cd frontend && npm run build

# フロントエンド開発サーバー
cd frontend && npm run dev
```

APIルートは `/api` プレフィックス。`/api/health` はDB接続確認込み（`database: ok/error` を返す）。

## アーキテクチャ

### データ階層（5層構造）
層(Layer) → カテゴリ(Category) → 単元(Unit) → 問題(Question) → 選択肢(Choice)

- 5層: 知識 / 文構造 / 読解基礎 / 読解応用 / 表現
- 13カテゴリ、41単元、**358問**（全問ファクトチェック済み）
- 単元コード例: `KN-001`(語彙), `TS-001`(時制), `VB-J1`(中1語彙), `RD-001`(読解), `JG-001`(中学基本文型), `EX-001`(表現)

### シードシステム（backend/seed/）
`seed_data.py` が起点で、`__main__` から全シードを連鎖実行する:
`seed()` → `seed_vocab` → `seed_reading` → `seed_junior` → `seed_extra` → `fix_misplaced_questions()` → `fix_question_content()`

**重要な規約:**
- シードは冪等。単元は `code`、問題は `question_text` の完全一致で重複スキップ
- **既存の問題文と同一の問題を追加するとサイレントにスキップされる**ので新規問題は文面を変えること
- seed_data.py のみ明示ID（layers/categories/units）を使うため、投入後にPostgreSQLシーケンスを `setval` で同期している（これを消すと本番で `duplicate key` になる）
- 既存DBの問題内容を修正するときは `CONTENT_FIXES`（seed_data.py）に追記する — 本番DBは再シードでは直らない
- 問題の品質基準: 正解はちょうど1つ / 選択肢の重複なし / 二重正解になる紛らわしい選択肢を置かない / 解説必須

### 学年対応
`diagnosis_service.py` の `GRADE_MAX_DIFFICULTY` が学年→出題難易度上限を定義
（中1・中2=1, 中3・高1=2, 高2・高3=3）。診断・弱点練習・解き直しすべてに適用。

### 主要API
- `POST /api/diagnosis/start` — 診断開始（20問、学年フィルタ付き）
- `POST /api/diagnosis/answer?session_id=&user_id=` — 回答（bodyは `question_id`, `selected_choice_id`）
- `POST /api/diagnosis/result?session_id=&user_id=` — 結果（弱点単元 + `study_points` 勉強法付き）
- `POST /api/diagnosis/weak-practice` — 弱点単元練習
- `POST /api/diagnosis/review-mistakes` — 解き直し（最後の回答が不正解のままの問題を出題）
- `GET /api/history/{user_id}/motivation` — ストリーク・XP/レベル・今日の目標・70日分ヒートマップ

### 学習継続機能
- ストリーク・日別集計は **JST基準**（history.py の `JST`）
- XP: 正解10pt / 不正解2pt、300XPごとにレベルアップ
- 弱点単元の勉強法は `backend/app/study_guides.py`（全41単元、各3項目）。単元を追加したら必ずここにも追記する

## デプロイ・運用

- **mainにマージ＝本番デプロイ**。作業ブランチは `claude/new-app-development-7une1v` を使い、動作確認後にmainへマージする
- Docker CMD はシード実行→gunicorn起動。シード失敗でもサーバーは起動する（DB障害時に port バインド失敗でデプロイが落ちないため）
- 起動時にRLS（Row-Level Security）を全テーブルに適用（Supabaseのセキュリティ要件）
- `.github/workflows/keepalive.yml` が6時間ごとに `/api/health` を叩き、**Supabase無料枠の自動一時停止を防止**（失敗時はGitHubからメール通知）
- Supabaseが `tenant not found` を返す場合はプロジェクトが一時停止中 → ダッシュボードで「Restore project」

## フロントエンド規約

- 画面は `frontend/src/pages/`（Home / Diagnosis / Results / Practice / Dashboard）
- APIクライアントは `frontend/src/api.js` に集約
- スタイルは `frontend/src/styles/global.css` のCSS変数（`--primary` 等）＋インラインstyle
- UX原則（デザインレビュー済み）:
  - 答え合わせは色だけに頼らない（○/✕マーク＋「正解：〜」テキスト明示）
  - 回答後も選択肢の文字は読める濃さを保つ（`.btn-choice:disabled` のスタイル）
  - 進行中の画面から離脱するボタンには確認ダイアログ
  - プライマリボタン背景は `--primary-dark`（WCAG AAコントラスト）
  - スコア0%のバーは最小幅3%で「計測済み」を可視化

## ユーザーとのコミュニケーション

このリポジトリのオーナーとのやり取りは**日本語**で行う。
