from ingestion.embedding import get_embedding
import json

def search(query, collections, n = 5):
    query_embed = get_embedding(query)

    results = collections.query(
        query_embeddings=[query_embed],
        n_results=n
    )

    resultDoc = {
        "question":query,
        "documents":[]
    }

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        resultDoc['documents'].append({
            'document':document,
            'metadata':metadata
        })
    
    if len(resultDoc["documents"]) == 0:
        resultDoc["documents"].append("No relevant data found in any of the sources")

    return json.dumps(resultDoc)