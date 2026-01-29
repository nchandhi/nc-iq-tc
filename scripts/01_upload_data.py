"""Upload PDF files to Azure AI Search with embeddings."""

import os
import json
import re
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    AzureOpenAIVectorizer,
    AzureOpenAIVectorizerParameters,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch,
)
from pypdf import PdfReader

# Load environment from azd
azure_dir = Path(__file__).parent.parent / ".azure"
env_name = os.environ.get("AZURE_ENV_NAME", "")
if not env_name and (azure_dir / "config.json").exists():
    with open(azure_dir / "config.json") as f:
        config = json.load(f)
        env_name = config.get("defaultEnvironment", "")

env_path = azure_dir / env_name / ".env"
if env_path.exists():
    load_dotenv(env_path)

INDEX_NAME = "documents"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def get_openai_client():
    """Create Azure OpenAI client."""
    endpoint = os.environ.get("AZURE_AI_ENDPOINT")
    if not endpoint:
        raise ValueError("AZURE_AI_ENDPOINT not set. Run 'azd up' first.")
    
    credential = DefaultAzureCredential()
    token = credential.get_token("https://cognitiveservices.azure.com/.default")
    
    return AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=token.token,
        api_version="2024-10-21",
    )


def get_search_clients():
    """Create Azure Search clients."""
    endpoint = os.environ.get("AZURE_AI_SEARCH_ENDPOINT")
    if not endpoint:
        raise ValueError("AZURE_AI_SEARCH_ENDPOINT not set")
    
    credential = DefaultAzureCredential()
    index_client = SearchIndexClient(endpoint, credential)
    search_client = SearchClient(endpoint, INDEX_NAME, credential)
    
    return index_client, search_client


def create_index(index_client: SearchIndexClient):
    """Create search index with vector search."""
    embedding_model = os.environ.get("AZURE_EMBEDDING_MODEL", "text-embedding-3-small")
    ai_endpoint = os.environ.get("AZURE_AI_ENDPOINT")
    
    fields = [
        SearchField(name="id", type=SearchFieldDataType.String, key=True),
        SearchField(name="content", type=SearchFieldDataType.String, searchable=True),
        SearchField(name="title", type=SearchFieldDataType.String, searchable=True, filterable=True),
        SearchField(name="source", type=SearchFieldDataType.String, filterable=True),
        SearchField(name="page_number", type=SearchFieldDataType.Int32, filterable=True, sortable=True),
        SearchField(name="chunk_id", type=SearchFieldDataType.Int32, sortable=True),
        SearchField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_profile_name="default-profile"
        ),
    ]
    
    vectorizer = AzureOpenAIVectorizer(
        vectorizer_name="openai-vectorizer",
        parameters=AzureOpenAIVectorizerParameters(
            resource_url=ai_endpoint,
            deployment_name=embedding_model,
            model_name=embedding_model,
        )
    )
    
    vector_search = VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="default-algorithm")],
        profiles=[VectorSearchProfile(
            name="default-profile",
            algorithm_configuration_name="default-algorithm",
            vectorizer_name="openai-vectorizer"
        )],
        vectorizers=[vectorizer]
    )
    
    semantic_config = SemanticConfiguration(
        name="default-semantic",
        prioritized_fields=SemanticPrioritizedFields(
            content_fields=[SemanticField(field_name="content")],
            title_field=SemanticField(field_name="title"),
        )
    )
    
    semantic_search = SemanticSearch(configurations=[semantic_config])
    
    index = SearchIndex(
        name=INDEX_NAME,
        fields=fields,
        vector_search=vector_search,
        semantic_search=semantic_search
    )
    index_client.create_or_update_index(index)
    print(f"Index '{INDEX_NAME}' ready")


def extract_pages_from_pdf(filepath: Path) -> list[tuple[int, str]]:
    """Extract text from PDF pages."""
    reader = PdfReader(filepath)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append((i + 1, text.strip()))
    return pages


def chunk_text(text: str, max_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence_len = len(sentence)
        
        if current_length + sentence_len > max_size and current_chunk:
            chunks.append(' '.join(current_chunk))
            # Keep overlap
            overlap_text = ' '.join(current_chunk)[-overlap:]
            current_chunk = [overlap_text] if overlap_text else []
            current_length = len(overlap_text)
        
        current_chunk.append(sentence)
        current_length += sentence_len
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks


def get_embedding(client: AzureOpenAI, text: str) -> list[float]:
    """Generate embedding for text."""
    model = os.environ.get("AZURE_EMBEDDING_MODEL", "text-embedding-3-small")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding


def main():
    data_dir = Path(__file__).parent.parent / "data"
    if not data_dir.exists():
        print("Creating data folder with sample documents...")
        data_dir.mkdir(exist_ok=True)
        # Create a simple text file as placeholder
        (data_dir / "sample.txt").write_text("This is sample content for testing.")
    
    pdf_files = list(data_dir.glob("*.pdf"))
    txt_files = list(data_dir.glob("*.txt"))
    
    if not pdf_files and not txt_files:
        print("No documents found in data folder.")
        return
    
    print(f"Found {len(pdf_files)} PDF(s) and {len(txt_files)} text file(s)")
    
    openai_client = get_openai_client()
    index_client, search_client = get_search_clients()
    
    create_index(index_client)
    
    documents = []
    
    # Process PDFs
    for pdf_path in pdf_files:
        print(f"Processing: {pdf_path.name}")
        pages = extract_pages_from_pdf(pdf_path)
        
        for page_num, page_text in pages:
            chunks = chunk_text(page_text)
            
            for chunk_idx, chunk in enumerate(chunks):
                doc_id = f"{pdf_path.stem}_p{page_num}_c{chunk_idx}"
                embedding = get_embedding(openai_client, chunk)
                
                doc = {
                    "id": doc_id,
                    "content": chunk,
                    "title": pdf_path.stem.replace("_", " ").title(),
                    "source": pdf_path.name,
                    "page_number": page_num,
                    "chunk_id": chunk_idx,
                    "embedding": embedding
                }
                documents.append(doc)
    
    # Process text files
    for txt_path in txt_files:
        print(f"Processing: {txt_path.name}")
        text = txt_path.read_text(encoding='utf-8')
        chunks = chunk_text(text)
        
        for chunk_idx, chunk in enumerate(chunks):
            doc_id = f"{txt_path.stem}_c{chunk_idx}"
            embedding = get_embedding(openai_client, chunk)
            
            doc = {
                "id": doc_id,
                "content": chunk,
                "title": txt_path.stem.replace("_", " ").title(),
                "source": txt_path.name,
                "page_number": 1,
                "chunk_id": chunk_idx,
                "embedding": embedding
            }
            documents.append(doc)
    
    print(f"\nUploading {len(documents)} chunks...")
    result = search_client.upload_documents(documents)
    succeeded = sum(1 for r in result if r.succeeded)
    print(f"Uploaded {succeeded}/{len(documents)} documents")
    print("Done!")


if __name__ == "__main__":
    main()
