# 1.3 Python Environment

## Create Virtual Environment

```bash
cd scripts
python -m venv .venv
```

## Activate Environment

=== "Windows"
    ```bash
    .venv\Scripts\activate
    ```

=== "macOS/Linux"
    ```bash
    source .venv/bin/activate
    ```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Verify Installation

```bash
python -c "import azure.ai.agents; print('Ready!')"
```

!!! success "Checkpoint"
    Before proceeding, verify:
    
    - [x] `azd up` completed successfully
    - [x] Resources visible in Azure Portal
    - [x] Python environment activated
