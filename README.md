# RAG_APP

Retrieval-Augmented Generation サンプルアプリケーション
LangChain + FAISS + Flask で構成。

## 必要環境

- Python 3.9〜3.11（※ 3.12 は一部未対応）
- pip
- 仮想環境推奨

## セットアップ手順（Windows/Mac 共通）

```bash
# 仮想環境の作成（オプション）
python -m venv venv
source venv/bin/activate  # Windowsは venv\Scripts\activate

# ライブラリのインストール
pip install flask langchain sentence-transformers faiss-cpu python-dotenv

# .env を作成（必要に応じて）
# 例: OPENAI_API_KEY=xxxxx

# FAISSインデックス作成
python create_faiss_index.py

# アプリ起動
python app.py
```
