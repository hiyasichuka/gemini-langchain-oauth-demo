# LangChain + Gemini OAuth Demo

このプロジェクトは、LangChain と Google Gemini API を使用するデモアプリケーションです。

## 前提条件

- Python 3.11 以上
- [uv](https://docs.astral.sh/uv/) がインストールされていること

uv のインストール:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# または Homebrew
brew install uv
```

## セットアップ

### 1. 依存関係のインストール

```bash
# uvで依存関係をインストール
uv sync
```

これにより、`.venv` 仮想環境が自動的に作成され、必要なパッケージがインストールされます。

## デモの実行方法

### オプション 1: Gemini API を使用したシンプルデモ（推奨）

最も簡単な方法です。Google Cloud Console の設定は不要です。

#### 1. API キーの取得

https://aistudio.google.com/app/apikey にアクセスして、無料の Gemini API キーを取得

#### 2. 環境変数の設定

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

#### 3. デモの実行

```bash
uv run python gemini_api_demo.py
```

### オプション 2: OAuth 認証を使用した FastAPI デモ

#### 1. Google Cloud Console での設定

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. プロジェクトを作成または選択
3. Vertex AI API を有効化
4. 「API とサービス」→「認証情報」→「認証情報を作成」→「OAuth クライアント ID」を選択
5. アプリケーションの種類で「ウェブアプリケーション」を選択
6. 承認済みのリダイレクト URI に `http://localhost:8000/oauth2callback` を追加
7. JSON をダウンロードして、プロジェクトのルートに `client_secret.json` として保存

#### 2. アプリケーションの実行

```bash
uv run uvicorn main:app --reload
```

#### 3. デモの使用

1. ブラウザで http://localhost:8000 にアクセス
2. http://localhost:8000/login にアクセスして Google 認証を行う
3. 認証後、http://localhost:8000/chat にアクセスして Gemini からのレスポンスを確認

## プロジェクト構成

```
.
├── gemini_api_demo.py    # シンプルな Gemini API デモ（推奨）
├── simple_demo.py        # Vertex AI を使用したデモ
├── main.py               # OAuth 認証付き FastAPI アプリ
├── pyproject.toml        # プロジェクト設定と依存関係
├── uv.lock               # uv ロックファイル
└── README.md             # このファイル
```

## 機能

- **シンプルデモ (`gemini_api_demo.py`)**

  - Gemini API を使用した LangChain の基本的な使い方
  - システムメッセージとユーザーメッセージの送信
  - 日本語での質疑応答

- **FastAPI デモ (`main.py`)**
  - FastAPI ベースの Web アプリケーション
  - Google OAuth 2.0 による認証
  - LangChain を使用した Gemini API へのアクセス
  - セッション管理によるユーザー認証状態の保持

## よく使う uv コマンド

```bash
# 依存関係のインストール/更新
uv sync

# パッケージの追加
uv add <package-name>

# パッケージの削除
uv remove <package-name>

# Python スクリプトの実行
uv run python <script.py>

# コマンドの実行
uv run <command>

# 仮想環境の有効化（手動で行う場合）
source .venv/bin/activate
```

## トラブルシューティング

### API キーが見つからない

`GOOGLE_API_KEY` 環境変数が設定されているか確認してください:

```bash
echo $GOOGLE_API_KEY
```

### モジュールが見つからない

依存関係を再インストールしてください:

```bash
uv sync --reinstall
```
