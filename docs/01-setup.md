[← Home](index) · [Module 2 →](02-foundry-iq)

# Module 1: Environment Setup

⏱️ **10 minutes** · Deploy Azure resources and set up your environment

---

## Step 1.1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/nchandhi/nc-iq-tc.git
cd nc-iq-tc
```

---

## Step 1.2: Login to Azure

Authenticate with Azure Developer CLI:

```bash
azd auth login
```

This will open a browser window for authentication.

---

## Step 1.3: Deploy Infrastructure

Deploy all required Azure resources:

```bash
azd up
```

When prompted:
- **Environment name**: Enter a unique name (e.g., `iq-lab-yourname`)
- **Azure subscription**: Select your subscription
- **Azure location**: Choose `eastus2` or `westus2` (recommended)

> ⏳ **Note**: Deployment takes approximately 5-7 minutes.

---

## Step 1.4: Verify Deployment

Once complete, you should see output similar to:

```
Deploying services (azd deploy)

  (✓) Done: Resource group: rg-iq-lab-yourname

SUCCESS: Your application was provisioned in Azure.
```

The following resources are created:
- **Azure AI Services** (Foundry IQ)
- **Azure AI Search** 
- **Storage Account**
- **Application Insights**

---

## Step 1.5: Set Up Python Environment

```bash
cd scripts
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ✅ Checkpoint

Before proceeding, verify:
- [ ] `azd up` completed successfully
- [ ] You can see resources in the Azure Portal
- [ ] Python virtual environment is activated

---

---

[← Home](index) · [**Next: Module 2 →**](02-foundry-iq)
