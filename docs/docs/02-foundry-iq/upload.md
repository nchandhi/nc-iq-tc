# Upload & Index Documents

## Upload to Search Index

```bash
python 01_upload_data.py
```

This script:

1. Reads documents from `data/` folder
2. Splits text into chunks (preserving sentence boundaries)
3. Generates vector embeddings using Azure OpenAI
4. Uploads to Azure AI Search with hybrid index (keyword + vector)

## Expected Output

```
Found 2 file(s)
Processing: contoso_products.txt
Processing: contoso_policies.txt
Uploading 12 chunks to search index...
Uploaded 12/12 documents
Done!
```

!!! tip "Using Your Own Documents"
    Add PDF or TXT files to the `data/` folder and re-run the script.
