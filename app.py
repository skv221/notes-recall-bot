from ingestion.loader import load_notes
from ingestion.chunker import chunk_doc
from ingestion.embedding import get_embedded_docs
from retrieval.search import search
from generation.llm import get_LLM_response
import chromadb
import time

client = chromadb.PersistentClient('./chroma_db')

collections = client.get_or_create_collection(
    name='notes'
)

if collections.count() == 0:
    print("Embedding is in progress....")
    documents = load_notes("notes")
    doc_chunks = chunk_doc(documents)
    doc_embeds = get_embedded_docs(doc_chunks)
    contents, metadata, embeds = [], [], []
    for doc in doc_embeds:
        contents.append(doc['content'])
        metadata.append({
            "filename":doc['filename'],
            "page no.":doc['page no.']
        })
        embeds.append(doc['embed'])
    collections.add(
        ids=[f'{i+1}' for i in range(len(doc_embeds))],
        documents=contents,
        metadatas=metadata,
        embeddings=embeds
    )
    print("Embedding process is done....")

print("-"*25)
time.sleep(2)
print("Greetings from Notes Recall Bot!!!")
time.sleep(2)
print("Recollect what you have learnt so far with the help of me...")
time.sleep(2)
print("Type Exit to leave the chat...")
time.sleep(2)
print("You are good to go....")
time.sleep(2)
print("-"*25)

while True:
    query = input('> ')
    if query.strip().lower() in ('exit', 'bye', ''):
        time.sleep(2)
        print("Bot: Thank you for using me... Please come back whenever you want to recollect your learnings... Have a nice day:)")
        print("-"*25)
        break
    result = search(query, collections)
    print(f"Bot is recollecting '{query}'.....")
    answer = get_LLM_response(result)
    time.sleep(3)
    print(f"\nBot: {answer}")
    print("-"*25)