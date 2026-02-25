from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.ingest import router as ingest_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="RAG Website Chatbot",
    version="1.0.0",
    description="Website URL ingestion + RAG chatbot backend"
)

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Routers ----------------
app.include_router(ingest_router, prefix="/ingest", tags=["Ingestion"])
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

# ---------------- Health ----------------
@app.get("/")
def home():
    return {
        "status": "running",
        "service": "RAG Website Chatbot API",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {"ok": True}


# ---------------- Local run ----------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
