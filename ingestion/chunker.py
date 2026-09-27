def chunk_doc(documents, chunk_size = 125, overlap = 20):
    doc_chunks = []
    for document in documents:
    
        words = document['content'].split()

        step = chunk_size - overlap

        for chunk_no, i in enumerate(range(0, len(words), step),start=1):
            chunk = " ".join(words[i:i+chunk_size])

            if chunk:
                doc_chunks.append({
                    "content":chunk,
                    "filename":document['filename'],
                    "page no.": chunk_no
                })
    
    return doc_chunks