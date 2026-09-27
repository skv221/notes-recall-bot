import requests

def get_embedding(text):
    response = requests.post(
        'http://localhost:11434/api/embed',
        json={
            'model':'nomic-embed-text',
            'input':text
        }
    )

    return response.json()['embeddings'][0]

def get_embedded_docs(doc_chunks):
    for i, doc in enumerate(doc_chunks):
        embed = get_embedding(doc['content'])
        doc['embed'] = embed
    return doc_chunks