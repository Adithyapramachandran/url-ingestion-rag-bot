# Integrate FAISS vector storage and similarity search
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

db = None

def get_db():
    global db

    if db is None:
        db = Chroma(
            collection_name="website",
            embedding_function=OpenAIEmbeddings(),
            persist_directory="./chroma"
        )

    return db
