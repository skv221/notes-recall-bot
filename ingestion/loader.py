from pathlib import Path

def load_notes(folder):
    documents = []

    for file_path in Path(folder).rglob("*.md"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        documents.append({
            "filename": file_path.name,
            "content": text
        })

    return documents