from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter

# テキスト（ローカル処理・API不要）
text = """
これはテスト用の文章です。
LangChainとFAISSを使って、検索可能なベクトルデータベースを構築します。
"""

documents = [Document(page_content=text)]

# テキスト分割
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(documents)

# ✅ HuggingFace Embeddings を使用（OpenAIではありません）
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# FAISSインデックス作成
db = FAISS.from_documents(split_docs, embeddings)

# 保存
db.save_local("faiss_index")
