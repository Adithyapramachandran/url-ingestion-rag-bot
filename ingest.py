from fastapi import APIRouter
from pydantic import BaseModel

from app.services.scraper import scrape_recursive
from app.services.chunking import chunk_text
from app.services.embeddings import store_documents

router = APIRouter(tags=["Ingestion"])   # ✅ REMOVE prefix


class URLRequest(BaseModel):
    url: str


@router.post("/")   # ✅ ADD slash
def ingest(req: URLRequest):
    texts = scrape_recursive(req.url, depth=1)
    chunks = chunk_text(texts)
    store_documents(chunks)

    return {"message": "Website indexed successfully"}