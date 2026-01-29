# Generate Sample Data

Before uploading documents and creating agents, you can generate **custom sample data** tailored to your business scenario.

## What Gets Generated

The script creates **both types of data** needed for the lab:

| Data Type | Format | Examples | Used By |
|-----------|--------|----------|---------|
| **Unstructured** | PDF documents | Policies, FAQs, procedures, guides | Foundry IQ (knowledge base) |
| **Structured** | CSV files | Customers, Products, Orders | Fabric IQ (ontology/NL→SQL) |

```
data/generated/
├── doc_01_return_policy.pdf      ← Unstructured (Foundry IQ)
├── doc_02_shipping_guide.pdf
├── customers.csv                  ← Structured (Fabric IQ)
├── products.csv
└── orders.csv
```

## Why Generate Custom Data?

The lab includes default Contoso Retail data, but you may want to:

- Test with data relevant to **your industry** (hospitality, finance, education)
- Create a **demo scenario** for stakeholders
- Explore how the AI handles **different business contexts**

## Choose a Scenario

Pick one of these pre-defined scenarios for the lab:

| # | Scenario | Industry | Best For |
|---|----------|----------|----------|
| 1 | **Contoso Electronics** | Retail | Product catalog, orders, customers |
| 2 | **Contoso Hotels** | Hospitality | Reservations, guests, loyalty |
| 3 | **Woodgrove Bank** | Finance | Accounts, loans, transactions |
| 4 | **Fabrikam Manufacturing** | Manufacturing | Inventory, suppliers, production |
| 5 | **Contoso University** | Education | Students, courses, faculty |

!!! tip "Recommended for Lab"
    Use **Scenario 1 (Retail)** for the lab. Experiment with others after completing the workshop.

## Run the Generator

Copy and run one of these commands:

=== "1. Retail (Recommended)"
    ```bash
    python scripts/00_generate_sample_data.py "Contoso Electronics retail store selling computers, phones, and accessories with online and in-store sales"
    ```

=== "2. Hospitality"
    ```bash
    python scripts/00_generate_sample_data.py "Contoso Hotels managing room reservations, guest services, and loyalty program rewards"
    ```

=== "3. Finance"
    ```bash
    python scripts/00_generate_sample_data.py "Woodgrove Bank handling customer accounts, loan applications, and transaction processing"
    ```

=== "4. Manufacturing"
    ```bash
    python scripts/00_generate_sample_data.py "Fabrikam Manufacturing tracking inventory, supplier orders, and production schedules"
    ```

=== "5. Education"
    ```bash
    python scripts/00_generate_sample_data.py "Contoso University managing student enrollment, course registration, and faculty assignments"
    ```

## Default Data Sizes

For fast lab execution, defaults are minimal:

| Data | Default Count | Environment Variable |
|------|---------------|---------------------|
| Documents | 2 | `NUM_DOCUMENTS` |
| Customers | 10 | `NUM_CUSTOMERS` |
| Products | 5 | `NUM_PRODUCTS` |
| Orders | 15 | `NUM_ORDERS` |

## Scale Up (Optional)

For more realistic demos, increase the counts:

```bash
# PowerShell
$env:NUM_DOCUMENTS=5; $env:NUM_CUSTOMERS=50; $env:NUM_ORDERS=100
python scripts/00_generate_sample_data.py "Your scenario"

# Bash
NUM_DOCUMENTS=5 NUM_CUSTOMERS=50 NUM_ORDERS=100 python scripts/00_generate_sample_data.py "Your scenario"
```

!!! tip "Keep It Small for Labs"
    Larger datasets take longer to process. Start small, then scale if needed.

## Next Steps

After generating data:

1. Review files in `data/generated/`
2. Continue to **Upload Data** step
