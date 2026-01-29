# Python Environment

## Create and Activate Environment

```bash
cd scripts
python -m venv .venv
```

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

## Verify Setup

```bash
python -c "import azure.ai.agents; print('Ready!')"
```

!!! success "Checkpoint"
    Before proceeding:
    
    - [x] `azd up` completed successfully
    - [x] Python environment activated
    - [x] Dependencies installed
