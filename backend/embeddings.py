from app.db.vector_store import get_db

def store_documents(chunks):
    db = get_db()
    db.add_texts(chunks)
