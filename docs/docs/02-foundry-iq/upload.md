# 2.1 Upload Documents

Upload sample documents to Azure AI Search for RAG.

## Run Upload Script

```bash
python 01_upload_data.py
```

## What This Does

1. Reads documents from `data/` folder
2. Chunks text with sentence-aware boundaries
3. Generates embeddings using Azure OpenAI
4. Uploads to Azure AI Search with vector indexing

## Expected Output

```
Found 2 PDF file(s)
Processing: contoso_products.txt
Processing: contoso_policies.txt
Uploading 12 chunks to search index...
Uploaded 12/12 documents
Done!
```

!!! info "Using Your Own Documents"
    You can add your own PDF or TXT files to the `data/` folder and re-run the script.
