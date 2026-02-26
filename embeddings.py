from app.db.vector_store import get_db

db = get_db()

def store_documents(chunks):

    if not chunks:
        return

    db.add_texts(chunks)