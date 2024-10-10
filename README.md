# ELYZA Japanese Chat Application

## 概要
このプロジェクトは、elyza/Llama-3-ELYZA-JP-8B-GGUFを使用したシンプルなUIのチャットアプリケーションです。

### 特徴
- OllamaベースのLlama-3-ELYZA-JP-8Bによる高品質な日本語応答
- 会話履歴を考慮した連続的な対話
- Dockerを使用した簡単なセットアップと実行
- StreamlitによるシンプルなUI

## 必要条件
- Docker と Docker Compose がインストールされていること
- 十分なディスク空き容量（モデルファイルのために約8GB）
- インターネット接続

## セットアップ手順

1. リポジトリのクローン
```bash
git clone https://github.com/MO-HU-P/elyza-chat-app.git
cd elyza-chat-app
```

2. ELYZAモデルのダウンロード
   - [elyza/Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF/tree/main) からモデルファイルをダウンロード
   - ダウンロードしたファイル `Llama-3-ELYZA-JP-8B-q4_k_m.gguf` をプロジェクトのルートディレクトリに配置

3. Dockerコンテナのビルドと起動
```bash
docker-compose up --build
```

## 使用方法
1. ブラウザで `http://localhost:8501` にアクセス
2. チャットインターフェースが表示されます
3. メッセージを入力して、AIアシスタントと会話を開始

## ファイル構成
- `app.py` - Streamlitを使用したチャットアプリケーションのメインコード
- `requirements.txt` - Pythonの依存パッケージリスト
- `Modelfile` - Ollamaのモデル設定ファイル
- `Dockerfile` - アプリケーションのDockerイメージ設定
- `docker-compose.yml` - マルチコンテナDockerアプリケーションの定義 

## トラブルシューティング

### よくある問題と解決方法
1. コンテナの起動確認: 
   ```bash
    docker-compose ps
   ```

2. コンテナが起動しない場合: ログの確認
   ```bash
   docker-compose logs -f
   ```

3. モデルのロードに失敗する場合:
   - モデルファイルが正しく配置されているか確認
   - Modelfileの内容が正しいか確認
   ```bash
    docker exec -it ollama-container ls
   ```

## 技術仕様
- フロントエンド: Streamlit
- バックエンド: Python, Langchain
- モデル: Llama-3-ELYZA-JP-8B-GGUF
- コンテナ化: Docker, Docker Compose

## 注意事項
- このアプリケーションは教育・研究目的で作成されています
- モデルの[ライセンス](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF)に従って使用してください

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。


