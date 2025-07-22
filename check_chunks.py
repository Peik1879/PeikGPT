from chromadb import PersistentClient

client = PersistentClient(path="D:\\PyCharm 2024.3.5\\Projects\\PeikGPT\\db")
collection = client.get_or_create_collection(name="peik_pdf")

results = collection.get(include=["documents", "metadatas"])

hits = []
for doc, meta in zip(results["documents"], results["metadatas"]):
    if "database" in doc.lower():
        hits.append((doc.strip(), meta))

print(f"\n✅ {len(hits)} Treffer gefunden mit dem Wort 'database'.")

for i, h in enumerate(hits[:10]):
    print(f"\nTreffer {i+1}:")
    print(f"[{h[1]['source']} – Seite {h[1]['seite']}]:\n")
    print(h[0][:500].replace("\n", " ") + "...")
