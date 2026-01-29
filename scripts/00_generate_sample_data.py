"""Generate sample data for both Foundry IQ and Fabric IQ based on a business scenario.

This script creates:
- PDF documents (unstructured) → for Foundry IQ knowledge base
- CSV files (structured) → for Fabric IQ ontology/NL→SQL

Usage:
    python 00_generate_sample_data.py "Your business scenario description"

=== RECOMMENDED SCENARIOS (pick one for the lab) ===

1. RETAIL (Default - Contoso Electronics)
   python 00_generate_sample_data.py "Contoso Electronics retail store selling computers, phones, and accessories with online and in-store sales"

2. HOSPITALITY (Hotel Chain)
   python 00_generate_sample_data.py "Contoso Hotels managing room reservations, guest services, and loyalty program rewards"

3. FINANCIAL SERVICES (Banking)
   python 00_generate_sample_data.py "Woodgrove Bank handling customer accounts, loan applications, and transaction processing"

4. MANUFACTURING (Supply Chain)
   python 00_generate_sample_data.py "Fabrikam Manufacturing tracking inventory, supplier orders, and production schedules"

5. EDUCATION (University)
   python 00_generate_sample_data.py "Contoso University managing student enrollment, course registration, and faculty assignments"

=== TIP: Use scenario #1 (Retail) for the lab, experiment with others later ===

Options (environment variables):
    NUM_DOCUMENTS=2      Number of PDF documents (default: 2)
    NUM_CUSTOMERS=10     Number of customer records (default: 10)
    NUM_PRODUCTS=5       Number of product records (default: 5)
    NUM_ORDERS=15        Number of order records (default: 15)
"""

import os
import sys
import json
import csv
import random
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

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


# =============================================================================
# CONFIGURATION - Adjust these for larger datasets
# =============================================================================

NUM_DOCUMENTS = int(os.environ.get("NUM_DOCUMENTS", "2"))   # PDFs for Foundry IQ
NUM_CUSTOMERS = int(os.environ.get("NUM_CUSTOMERS", "10"))  # Customer records
NUM_PRODUCTS = int(os.environ.get("NUM_PRODUCTS", "5"))     # Product records
NUM_ORDERS = int(os.environ.get("NUM_ORDERS", "15"))        # Order records


# =============================================================================
# AI CLIENT
# =============================================================================

def get_project_client():
    """Create AI Foundry Project client using endpoint."""
    endpoint = os.environ.get("AZURE_AI_PROJECT_ENDPOINT")
    if not endpoint:
        raise ValueError("AZURE_AI_PROJECT_ENDPOINT not set. Run 'azd up' first.")
    
    return AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=endpoint,
    )


def call_ai(client: AIProjectClient, prompt: str) -> str:
    """Call AI model and return response text."""
    model = os.environ.get("AZURE_CHAT_MODEL", "gpt-4o-mini")
    
    agent = client.agents.create_agent(
        model=model,
        name="data-generator",
        instructions="You are a helpful data generation assistant. Follow instructions exactly and return only the requested format."
    )
    
    try:
        thread = client.agents.threads.create()
        client.agents.messages.create(thread_id=thread.id, role="user", content=prompt)
        client.agents.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
        
        messages = client.agents.messages.list(thread_id=thread.id)
        for msg in messages:
            if msg.role == "assistant":
                return msg.content[0].text.value
        return ""
    finally:
        client.agents.delete_agent(agent.id)


# =============================================================================
# FOUNDRY IQ: UNSTRUCTURED DATA (PDFs)
# =============================================================================

def generate_documents(client: AIProjectClient, scenario: str, data_dir: Path):
    """Generate PDF documents for Foundry IQ knowledge base."""
    print(f"\n📄 Generating {NUM_DOCUMENTS} PDF documents for Foundry IQ...")
    
    # Check for reportlab
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        has_reportlab = True
    except ImportError:
        has_reportlab = False
        print("   (reportlab not installed - creating .txt files instead)")
    
    # Get document topics
    prompt = f"""For a business scenario: "{scenario}"

Generate exactly {NUM_DOCUMENTS} document topics that would be useful for a knowledge base.
These should be policy documents, guides, FAQs, or procedures.

Return ONLY a JSON array of objects with "title" and "description" fields.
Example: [{{"title": "Return Policy", "description": "Guidelines for product returns"}}]"""

    response = call_ai(client, prompt)
    
    try:
        # Extract JSON from response
        start = response.find("[")
        end = response.rfind("]") + 1
        topics = json.loads(response[start:end])
    except:
        topics = [{"title": f"Document {i}", "description": scenario} for i in range(1, NUM_DOCUMENTS + 1)]
    
    for i, topic in enumerate(topics[:NUM_DOCUMENTS], 1):
        print(f"   Creating document {i}/{NUM_DOCUMENTS}: {topic['title']}")
        
        content_prompt = f"""Write a detailed business document for: {topic['title']}
Business context: {scenario}
Description: {topic.get('description', '')}

Write 3-4 paragraphs (300-400 words total) of professional business content.
Include specific policies, procedures, or guidelines as appropriate.
Do not include any markdown formatting - just plain text paragraphs."""

        content = call_ai(client, content_prompt)
        
        filename = f"doc_{i:02d}_{topic['title'].lower().replace(' ', '_')[:30]}"
        
        if has_reportlab:
            filepath = data_dir / f"{filename}.pdf"
            create_pdf(filepath, topic['title'], content)
        else:
            filepath = data_dir / f"{filename}.txt"
            with open(filepath, "w") as f:
                f.write(f"{topic['title']}\n{'='*len(topic['title'])}\n\n{content}")
        
        print(f"   ✓ Created: {filepath.name}")


def create_pdf(filepath: Path, title: str, content: str):
    """Create a PDF file with the given content."""
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    
    doc = SimpleDocTemplate(str(filepath), pagesize=letter)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20
    )
    
    story = []
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    
    for para in content.split("\n\n"):
        if para.strip():
            story.append(Paragraph(para.strip(), styles['Normal']))
            story.append(Spacer(1, 12))
    
    doc.build(story)


# =============================================================================
# FABRIC IQ: STRUCTURED DATA (CSVs)
# =============================================================================

def generate_structured_data(client: AIProjectClient, scenario: str, data_dir: Path):
    """Generate CSV files for Fabric IQ ontology/NL→SQL."""
    print(f"\n📊 Generating structured data for Fabric IQ...")
    
    # Get entity names and attributes based on scenario
    schema_prompt = f"""For a business scenario: "{scenario}"

Define 3 main business entities that would be tracked in a database.
For each entity, provide realistic column names and sample values.

Return ONLY valid JSON in this exact format:
{{
  "entities": [
    {{
      "name": "EntityName",
      "columns": ["Column1", "Column2", "Column3"],
      "sample_values": ["value1", "value2", "value3"]
    }}
  ]
}}

Make entities related (e.g., Customers, Products, Orders/Transactions)."""

    response = call_ai(client, schema_prompt)
    
    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        schema = json.loads(response[start:end])
        entities = schema.get("entities", [])
    except:
        # Fallback to generic business entities
        entities = [
            {"name": "Customers", "columns": ["CustomerID", "Name", "Email", "Segment", "Region"]},
            {"name": "Products", "columns": ["ProductID", "Name", "Category", "Price", "Stock"]},
            {"name": "Orders", "columns": ["OrderID", "CustomerID", "ProductID", "Quantity", "Total", "Date"]}
        ]
    
    # Generate data for each entity
    for entity in entities[:3]:  # Limit to 3 entities
        entity_name = entity["name"]
        columns = entity.get("columns", ["ID", "Name", "Value"])[:6]  # Limit columns
        
        # Determine row count based on entity type
        if "customer" in entity_name.lower():
            row_count = NUM_CUSTOMERS
        elif "product" in entity_name.lower() or "item" in entity_name.lower():
            row_count = NUM_PRODUCTS
        else:
            row_count = NUM_ORDERS
        
        print(f"   Creating {entity_name} ({row_count} rows)...")
        
        data_prompt = f"""Generate exactly {row_count} rows of realistic sample data for a "{entity_name}" table.
Business context: {scenario}
Columns: {', '.join(columns)}

Return ONLY a valid JSON array of objects. Each object should have these exact keys: {columns}
Use realistic values appropriate for the business scenario.
For IDs, use sequential numbers starting from 1.
For dates, use format YYYY-MM-DD within the last 12 months.
For prices/amounts, use reasonable numbers with 2 decimal places.

Example format: [{{"Column1": "value1", "Column2": "value2"}}]"""

        response = call_ai(client, data_prompt)
        
        try:
            start = response.find("[")
            end = response.rfind("]") + 1
            rows = json.loads(response[start:end])
        except:
            # Generate fallback data
            rows = generate_fallback_data(entity_name, columns, row_count)
        
        # Write CSV
        filename = f"{entity_name.lower().replace(' ', '_')}.csv"
        filepath = data_dir / filename
        
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            for row in rows[:row_count]:
                # Ensure all columns exist
                clean_row = {col: row.get(col, "") for col in columns}
                writer.writerow(clean_row)
        
        print(f"   ✓ Created: {filename}")


def generate_fallback_data(entity_name: str, columns: list, count: int) -> list:
    """Generate fallback data if AI fails."""
    rows = []
    base_date = datetime.now()
    
    for i in range(1, count + 1):
        row = {}
        for col in columns:
            col_lower = col.lower()
            if "id" in col_lower:
                row[col] = i
            elif "name" in col_lower:
                row[col] = f"{entity_name[:-1] if entity_name.endswith('s') else entity_name} {i}"
            elif "email" in col_lower:
                row[col] = f"user{i}@example.com"
            elif "price" in col_lower or "total" in col_lower or "amount" in col_lower:
                row[col] = round(random.uniform(10, 500), 2)
            elif "quantity" in col_lower or "stock" in col_lower:
                row[col] = random.randint(1, 100)
            elif "date" in col_lower:
                days_ago = random.randint(1, 365)
                row[col] = (base_date - timedelta(days=days_ago)).strftime("%Y-%m-%d")
            elif "category" in col_lower or "segment" in col_lower or "region" in col_lower:
                options = ["A", "B", "C"]
                row[col] = random.choice(options)
            else:
                row[col] = f"Value {i}"
        rows.append(row)
    
    return rows


# =============================================================================
# MAIN
# =============================================================================

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n" + "="*60)
        print("ERROR: Please provide a business scenario description.")
        print("="*60)
        sys.exit(1)
    
    scenario = " ".join(sys.argv[1:])
    
    print("="*60)
    print("SAMPLE DATA GENERATOR")
    print("="*60)
    print(f"\nScenario: {scenario}")
    print(f"\nData sizes (adjust via environment variables):")
    print(f"  • Documents (PDFs):  {NUM_DOCUMENTS}  (NUM_DOCUMENTS)")
    print(f"  • Customers:         {NUM_CUSTOMERS}  (NUM_CUSTOMERS)")
    print(f"  • Products:          {NUM_PRODUCTS}   (NUM_PRODUCTS)")
    print(f"  • Orders:            {NUM_ORDERS}  (NUM_ORDERS)")
    
    # Create data folder
    data_dir = Path(__file__).parent.parent / "data" / "generated"
    data_dir.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput folder: {data_dir}")
    
    # Get AI client
    client = get_project_client()
    
    # Generate both types of data
    generate_documents(client, scenario, data_dir)
    generate_structured_data(client, scenario, data_dir)
    
    print("\n" + "="*60)
    print("✅ DATA GENERATION COMPLETE")
    print("="*60)
    print(f"\nGenerated files in: {data_dir}")
    print("\nNext steps:")
    print("  1. Review generated files in data/generated/")
    print("  2. Run '01_upload_data.py' to upload PDFs to knowledge base")
    print("  3. Run '04a_create_ontology.py' to create ontology from CSVs")
    print("\nTo generate larger datasets, set environment variables:")
    print("  NUM_DOCUMENTS=10 NUM_CUSTOMERS=100 NUM_ORDERS=500 python 00_generate_sample_data.py \"...\"")


if __name__ == "__main__":
    main()
