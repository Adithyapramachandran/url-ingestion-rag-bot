def chunk_text(pages, size=500):
    chunks = []
    for page in pages:
        for i in range(0, len(page), size):
            chunks.append(page[i:i+size])
    return chunks
