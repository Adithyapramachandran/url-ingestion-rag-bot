# Implement text chunking with overlap support
def chunk_text(texts,size=500,overlap=100):
    chunks=[]
    for t in texts:
        start=0
        while start<len(t):
            chunks.append(t[start:start+size])
            start+=size-overlap
    return chunks
