# Foundry IQ & Fabric IQ Lab

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/nchandhi/nc-iq-tc)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/nchandhi/nc-iq-tc)

**🔗 Lab Guide: [https://nchandhi.github.io/nc-iq-tc](https://nchandhi.github.io/nc-iq-tc)**

A 50-minute hands-on lab for building AI solutions with Microsoft Foundry IQ and Fabric IQ.

## Overview

This lab demonstrates building an end-to-end AI solution that:
- Uses **Foundry IQ** to create intelligent AI agents
- Connects to enterprise data via **Fabric IQ**
- Implements RAG (Retrieval-Augmented Generation) with Azure AI Search
- Includes quality and safety evaluations

## Prerequisites

- Azure subscription with Contributor access
- [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- Python 3.10+

## Quick Start

```bash
# Clone and deploy
git clone https://github.com/nchandhi/nc-iq-tc.git
cd nc-iq-tc
azd auth login
azd up

# Set up Python environment
cd scripts
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Run the lab
python 01_upload_data.py
python 02_create_agent.py
python 03_test_agent.py
```

## Lab Modules

| Module | Duration | Description |
|--------|----------|-------------|
| [1. Setup](https://nchandhi.github.io/nc-iq-tc/01-setup) | 10 min | Deploy Azure resources |
| [2. Foundry IQ](https://nchandhi.github.io/nc-iq-tc/02-foundry-iq) | 15 min | Create AI agent |
| [3. Fabric IQ](https://nchandhi.github.io/nc-iq-tc/03-fabric-iq) | 10 min | Connect data sources |
| [4. Testing](https://nchandhi.github.io/nc-iq-tc/04-integration) | 10 min | Run evaluations |
| [5. Cleanup](https://nchandhi.github.io/nc-iq-tc/05-cleanup) | 5 min | Delete resources |

## Cleanup

```bash
azd down
```

## License

MIT License - see [LICENSE](LICENSE)