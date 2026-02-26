from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(texts):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    docs = splitter.create_documents(texts)

    return [d.page_content for d in docs]