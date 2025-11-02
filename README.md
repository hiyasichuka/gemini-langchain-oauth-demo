# LangChain + Gemini OAuth Demo

このプロジェクトは、LangChain と Google Gemini API を OAuth 認証で使用するデモアプリケーションです。

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -e .
```

### 2. Google Cloud Console での設定

1. [Google Cloud Console](https://console.cloud.google.com/) にアクセス
2. プロジェクトを作成または選択
3. Vertex AI API を有効化
4. 「API とサービス」→「認証情報」→「認証情報を作成」→「OAuth クライアント ID」を選択
5. アプリケーションの種類で「ウェブアプリケーション」を選択
6. 承認済みのリダイレクト URI に `http://localhost:8000/oauth2callback` を追加
7. JSON をダウンロードして、プロジェクトのルートに `client_secret.json` として保存

### 3. アプリケーションの実行

```bash
uvicorn main:app --reload
```

### 4. デモの使用

1. ブラウザで http://localhost:8000 にアクセス
2. http://localhost:8000/login にアクセスして Google 認証を行う
3. 認証後、http://localhost:8000/chat にアクセスして Gemini からのレスポンスを確認

## 機能

- FastAPI ベースの Web アプリケーション
- Google OAuth 2.0 による認証
- LangChain を使用した Gemini API へのアクセス
- セッション管理によるユーザー認証状態の保持
