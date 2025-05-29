from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms.base import LLM
from dotenv import load_dotenv

load_dotenv()

# ローカル埋め込みモデル（無料）
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.load_local("rag_app/faiss_index", embeddings, allow_dangerous_deserialization=True)

# ローカルLLM（ダミー応答用）
class DummyLLM(LLM):
    def _call(self, prompt, stop=None):
        return "（ダミー応答）これは社内資料の内容に基づく自動回答です。"

    @property
    def _llm_type(self):
        return "dummy"

llm = DummyLLM()

prompt = PromptTemplate.from_template("以下の文章を参考に質問に答えてください。\n\n{context}\n\n質問: {question}\n\n回答:")

chain = LLMChain(llm=llm, prompt=prompt)

def get_answer(question):
    docs = db.similarity_search(question)
    context = "\n".join([doc.page_content for doc in docs])
    answer = chain.run({"context": context, "question": question})
    return answer
