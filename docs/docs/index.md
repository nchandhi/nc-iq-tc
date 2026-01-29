# Foundry IQ & Fabric IQ Lab

> **⏱️ 50 minutes** · **👥 50-100 participants**

Build an end-to-end AI solution using Microsoft Foundry IQ and Fabric IQ.

## What You'll Build

- ✅ Deploy Azure AI Foundry resources using Infrastructure as Code
- ✅ Create a RAG-enabled AI agent with Foundry IQ
- ✅ Connect to enterprise data using Fabric IQ
- ✅ Test and validate your AI solution

## Prerequisites

- Azure subscription with Contributor access
- [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- [Python 3.10+](https://www.python.org/downloads/)

## Lab Modules

| Module | Description | Time |
|--------|-------------|------|
| [01 Setup](01-setup/index.md) | Deploy Azure resources | 10 min |
| [02 Foundry IQ](02-foundry-iq/index.md) | Create AI Agent | 15 min |
| [03 Fabric IQ](03-fabric-iq/index.md) | Connect Data | 10 min |
| [04 Testing](04-testing/index.md) | Run Evaluations | 10 min |
| [05 Cleanup](05-cleanup/index.md) | Delete Resources | 5 min |

## Quick Start

```bash
git clone https://github.com/nchandhi/nc-iq-tc.git
cd nc-iq-tc
azd auth login
azd up
```

[**Start Lab →**](01-setup/index.md)
