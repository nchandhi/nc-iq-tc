# Foundry IQ & Fabric IQ Lab

**⏱️ Duration: 50 minutes** | **👥 Audience: 50-100 participants**

Build an end-to-end AI solution using Microsoft Foundry IQ and Fabric IQ. This hands-on lab walks you through creating an intelligent agent that leverages enterprise data.

---

## 🎯 What You'll Build

By the end of this lab, you will have:
- Deployed Azure AI Foundry resources using Infrastructure as Code
- Created a RAG-enabled AI agent with Foundry IQ
- Connected to enterprise data using Fabric IQ
- Tested and validated your AI solution

---

## 📋 Prerequisites

- Azure subscription with Contributor access
- [Azure Developer CLI (azd)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) installed
- [Python 3.10+](https://www.python.org/downloads/) installed
- [VS Code](https://code.visualstudio.com/) (recommended)

---

## 🗂️ Lab Modules

| Module | Title | Duration |
|--------|-------|----------|
| 1 | [Environment Setup](01-setup.md) | 10 min |
| 2 | [Foundry IQ - Create AI Agent](02-foundry-iq.md) | 15 min |
| 3 | [Fabric IQ - Connect Data](03-fabric-iq.md) | 10 min |
| 4 | [Integration & Testing](04-integration.md) | 10 min |
| 5 | [Cleanup](05-cleanup.md) | 5 min |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/nchandhi/nc-iq-tc.git
cd nc-iq-tc

# Login and deploy
azd auth login
azd up
```

---

## 📚 Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Microsoft Fabric Documentation](https://learn.microsoft.com/fabric/)
- [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/)

---

**Ready to start?** [Begin with Module 1: Environment Setup →](01-setup.md)
