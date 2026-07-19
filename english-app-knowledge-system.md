# 英語学習アプリ プロジェクト起動チェックリスト
## tohon English Diagnosis - Project Initialization

---

## 📚 完成したドキュメント一覧

### 1️⃣ 知識体系設計
**ファイル**: `english-app-knowledge-system.md`
**内容**:
- NextStage完全マッピング（層1～5）
- 単元ツリー構造（全190単元以上）
- 各単元のよくある誤答パターン
- 前提知識・依存関係の定義

**用途**:
- DBスキーマ設計時に参照
- 問題生成時のコンテキスト
- 診断ロジック設計時に参照

---

### 2️⃣ AI問題生成システム
**ファイル**: `ai-problem-generation-system.md`
**内容**:
- 層別のプロンプトテンプレート（6パターン）
- 問題生成パイプライン（実装コード例）
- 問題数見積もり（1640～1840問）
- 運用フロー（生成→レビュー→登録）

**用途**:
- Claude / ChatGPT API の呼び出し実装時に参照
- 生成AIの prompt engineering ガイド
- 問題生成スクリプトの実装テンプレート

---

### 3️⃣ 実装設計
**ファイル**: `implementation-design.md`
**内容**:
- システムアーキテクチャ図
- DB スキーマ（全9テーブル、完全なSQL例）
- 診断ロジック（アルゴリズム詳細）
- API 仕様（6エンドポイント）
- 技術スタック提案

**用途**:
- バックエンド実装時に参照
- DB 設計・ORMマッピング時に参照
- API 設計の specification
- 診断アルゴリズム実装時の pseudocode

---

### 4️⃣ 実装ロードマップ
**ファイル**: `implementation-roadmap.md`
**内容**:
- Phase 1 (MVP) の週単位タスク（Week 1～12）
- 各週のタスク詳細＋実装例コード
- Week 別の成果物定義
- 工数見積もり
- 外注検討項目

**用途**:
- プロジェクト管理・スケジューリング
- チームメンバーへのタスク割り当て
- 進捗追跡

---

## 🎯 実装開始前チェックリスト

### ステップ1: 意思決定（今日中に）

#### 1-1 開発環境の選択
- [ ] **バックエンド言語を決定**
  ```
  選択肢:
  ☐ Python (FastAPI) ← 推奨
  ☐ Node.js (Express)
  ☐ Go (Gin)
  
  決定: _____________
  ```

- [ ] **フレームワークを決定**
  ```
  推奨: FastAPI (Python の場合)
  決定: _____________
  ```

- [ ] **フロントエンドフレームワークを決定**
  ```
  選択肢:
  ☐ React ← 推奨
  ☐ Vue.js
  ☐ Flutter (モバイルも同時)
  
  決定: _____________
  ```

- [ ] **データベースを決定**
  ```
  選択肢:
  ☐ PostgreSQL ← 推奨
  ☐ MySQL
  
  決定: _____________
  ```

- [ ] **ホスティング環境を決定**
  ```
  選択肢:
  ☐ AWS ← 推奨
  ☐ Google Cloud
  ☐ Azure
  ☐ Heroku (小規模・趣味向け)
  
  決定: _____________
  ```

---

#### 1-2 外注判断
- [ ] **UI/UX デザイン**
  ```
  ☐ 自作する
  ☐ 外注する（10～20万円）
  
  決定: _____________
  ```

- [ ] **フロント開発**
  ```
  ☐ 自作する
  ☐ 一部外注する（20～40万円）
  ☐ 全外注する（80～120万円）
  
  決定: _____________
  ```

- [ ] **問題の人手レビュー**
  ```
  ☐ 自分でやる
  ☐ 外注する（10～30万円）
  
  決定: _____________
  ```

---

#### 1-3 開発体制
- [ ] **1人で開発するか、チームを組むか**
  ```
  ☐ 1人（フルスタック）
  ☐ 2人（フロント+バック）
  ☐ 3人以上（分業体制）
  
  決定: _____________
  ```

- [ ] **進捗管理ツール**
  ```
  選択肢:
  ☐ GitHub Projects
  ☐ Trello
  ☐ Jira
  ☐ Notion
  
  決定: _____________
  ```

---

### ステップ2: 環境構築（Week 1）

#### 2-1 PC 環境
- [ ] **Python 3.10+ をインストール** (バックエンド担当者)
  ```bash
  python --version  # 確認
  ```

- [ ] **Node.js 18+ をインストール** (フロント担当者)
  ```bash
  node --version    # 確認
  ```

- [ ] **PostgreSQL インストール＆起動** (DB担当者)
  ```bash
  psql --version    # 確認
  ```

- [ ] **Git インストール**
  ```bash
  git --version     # 確認
  ```

- [ ] **IDE/エディタをセットアップ**
  ```
  選択肢:
  ☐ VS Code
  ☐ PyCharm (Python)
  ☐ WebStorm (JavaScript)
  ☐ IntelliJ IDEA (全般)
  
  決定: _____________
  ```

---

#### 2-2 API キー取得
- [ ] **Anthropic API キー取得**
  ```
  URL: https://console.anthropic.com/
  キー: sk-ant-... (メモに保存)
  ✓ 確認日時: __________
  ```

- [ ] **CloudFlare (CDN/DNS)** (オプション)
  ```
  URL: https://dash.cloudflare.com/
  ```

---

#### 2-3 ソースコード管理
- [ ] **GitHub リポジトリ作成**
  ```
  URL: https://github.com/new
  リポジトリ名: english-diagnosis-app
  ✓ 作成日時: __________
  ```

- [ ] **.gitignore 設定**
  ```
  追加する除外ファイル:
  - .env
  - venv/
  - node_modules/
  - .DS_Store
  - *.pyc
  ```

- [ ] **ブランチ戦略決定**
  ```
  推奨:
  - main: 本番環境
  - develop: 開発環境
  - feature/*: 機能開発
  
  決定: _____________
  ```

---

### ステップ3: プロジェクト初期化（Week 1）

#### 3-1 バックエンド
- [ ] **プロジェクトフォルダ作成**
  ```bash
  mkdir english-diagnosis-api
  cd english-diagnosis-api
  git init
  ```

- [ ] **Python 仮想環境作成**
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # Linux/Mac
  # または venv\Scripts\activate (Windows)
  ```

- [ ] **requirements.txt 作成**
  ```
  fastapi
  uvicorn
  sqlalchemy
  psycopg2-binary  # PostgreSQL ドライバ
  pydantic
  python-dotenv
  anthropic
  ```

- [ ] **ライブラリインストール**
  ```bash
  pip install -r requirements.txt
  ```

- [ ] **.env ファイル作成**
  ```
  DATABASE_URL=postgresql://user:password@localhost:5432/english_app
  ANTHROPIC_API_KEY=sk-ant-...
  FRONTEND_URL=http://localhost:3000
  ```

---

#### 3-2 フロント
- [ ] **React プロジェクト作成**
  ```bash
  npx create-react-app english-diagnosis-frontend
  cd english-diagnosis-frontend
  ```

- [ ] **必要なライブラリインストール**
  ```bash
  npm install axios react-router-dom
  npm install --save-dev tailwindcss postcss autoprefixer  # スタイリング
  ```

- [ ] **.env 作成**
  ```
  REACT_APP_API_URL=http://localhost:8000/api
  ```

---

#### 3-3 データベース
- [ ] **PostgreSQL DB 作成**
  ```sql
  CREATE DATABASE english_app;
  ```

- [ ] **ユーザー作成**
  ```sql
  CREATE USER english_user WITH PASSWORD 'password';
  GRANT ALL PRIVILEGES ON DATABASE english_app TO english_user;
  ```

---

### ステップ4: 初期データ準備（Week 2）

#### 4-1 マスタデータ JSON 作成

- [ ] **layers.json（5行）**
  ```json
  [
    {"layer_id": 1, "layer_name": "知識", "order_priority": 1},
    ...
  ]
  ```

- [ ] **units.json（190+行）**
  - ドキュメント「知識体系マッピング」から抽出
  ```json
  [
    {"unit_id": "TS-001", "unit_name": "現在形", "layer_id": 2, ...},
    ...
  ]
  ```

---

#### 4-2 初期問題データ

- [ ] **テスト用ダミー問題を 50～100 問作成**
  - 層1: 20問
  - 層2（時制）: 30問
  - 層2（態）: 20問
  - その他: 10問

**方法**: 
1. Anthropic API で生成
2. 手動で 10～15% レビュー
3. DB に投入

---

### ステップ5: 実装体制の整備（Week 1-2）

#### 5-1 チーム連携
- [ ] **Slack / Discord ワークスペース作成**
- [ ] **毎日のスタンドアップミーティング時間決定**
  ```
  推奨: 朝 9:00 (15分)
  決定: _____________
  ```

- [ ] **GitHub で Issue・PR レビュープロセス決定**

#### 5-2 ドキュメント管理
- [ ] **本ドキュメントをチーム全員が確認**
  - 最低限: Roadmap と Design の確認必須
  
- [ ] **プロジェクト Wiki 作成**
  - GitHub Wiki / Notion など
  - セットアップ手順
  - API ドキュメント
  - トラブルシューティング

---

## 📋 実装開始時の最終確認

実装開始の前に、以下の確認を取ってください：

```
【1. 開発言語・フレームワーク】
バックエンド: ________________________
フロント: ________________________
DB: ________________________
ホスティング: ________________________

【2. 開発人数・体制】
開発者数: ___人
進捗管理ツール: ________________________

【3. API キー】
Anthropic キー取得状況: ☐ 完了 / ☐ 準備中 / ☐ 未着手
取得日時: ________________________

【4. リポジトリ】
GitHub URL: ________________________
初期化完了: ☐ 完了 / ☐ 準備中 / ☐ 未着手

【5. 開発環境**
Python / Node.js インストール: ☐ 完了
PostgreSQL インストール: ☐ 完了
IDE セットアップ: ☐ 完了

【6. 開始予定日】
実装開始予定日: ________________________
```

---

## 🚀 Week 1 の最初のタスク（Day 1）

### 朝一（1時間）
1. 上記チェックリストの「ステップ1：意思決定」を全て完了
2. GitHub リポジトリを作成
3. チーム（1人の場合は自分）に伝達

### 午前中（2～3時間）
1. Python 仮想環境をセットアップ
2. 必要なライブラリをインストール
3. FastAPI で簡単な `GET /api/health` を実装してテスト

### 午後（2～3時間）
1. React プロジェクトを作成
2. PostgreSQL DB を作成
3. 簡単な画面（トップページ）を作成

### Day 1 終了時の目標
- [ ] バックエンド: `http://localhost:8000/api/health` が応答する
- [ ] フロント: `http://localhost:3000` でトップページが表示される
- [ ] DB: 接続確認完了

---

## 📞 トラブルシューティング

### Python・FastAPI のインストール後、import エラーが出た場合
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### PostgreSQL 接続エラー
```bash
# ローカル DB の確認
psql -U english_user -d english_app
```

### React のビルドエラー
```bash
rm -rf node_modules
rm package-lock.json
npm install
npm start
```

---

## 📞 連絡先・サポート

### トラブルシューティング
- **Claude に相談**: このチェックリスト内容に加えて、エラーメッセージを共有
- **公式ドキュメント**:
  - FastAPI: https://fastapi.tiangolo.com/
  - React: https://react.dev/
  - PostgreSQL: https://www.postgresql.org/docs/

---

## ✅ プロジェクト完成までの見通し

```
Week 1-2: 環境構築 ✓
Week 3-4: バックエンド基本実装 ✓
Week 5-6: フロント実装 ✓
Week 7-8: AI 問題生成＆統合テスト ✓
Week 9-10: 診断ロジック実装 ✓
Week 11-12: ホスティング・本番準備 ✓

MVP ローンチ: Week 12 終了時
```

**合計: 12週間（約3ヶ月）**

---

## 🎉 Next Step

1. **このチェックリストを完了する**
2. **開発環境をセットアップする**
3. **Week 1 タスクを開始する**

Good luck! 🚀