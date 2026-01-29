# Lab Creation Guide

Instructions for creating hands-on labs hosted on GitHub Pages using MkDocs Material.

## Reference Lab

**Example**: [Foundry IQ + Fabric IQ Lab](https://nchandhi.github.io/nc-iq-tc) | [Source](https://github.com/nchandhi/nc-iq-tc)

Use this lab as the canonical example for content structure, navigation, and style.

## Goal

Create a professional, easy-to-maintain lab site that:
- Is hosted on GitHub.io (free, auto-deploys)
- Uses simple markdown files (no complex build systems)
- Has modern navigation with tabs and sidebar
- Can be customized for different Solution Accelerator scenarios

## Platform & Tooling

- **Documentation**: MkDocs Material theme
- **Hosting**: GitHub Pages (enable in repo Settings → Pages → Source: GitHub Actions)
- **Format**: Markdown files only (keep it simple)
- **Navigation**: Tabs (top) + sidebar (left) for modules
- **Auto-deploy**: GitHub Actions workflow deploys on push to main

## Naming Convention

**Title format**: `Build faster with Solution Accelerators – [Product Names] (Hands-on lab)`

Example: `Build faster with Solution Accelerators – Foundry IQ + Fabric IQ (Hands-on lab)`

## Introduction Page Must Include

1. **Opening line**: "Learn how to [action] that [benefit]"
2. **Solution accelerators pitch**: "Solution accelerators provide ready-to-deploy templates to get you from idea to working solution quickly, then customize it for your industry use case."
3. **The Opportunity**: Business problem being solved
4. **The Solution**: What the products do (bullet list)
5. **What You'll Build**: Table with Component | Technology | Purpose
6. **Prerequisites**: Required tools and access
7. **Start Lab link**

## Writing Guidelines

### Do
- Use positive, capability-focused language
- Frame as "enables", "provides", "helps"
- Keep sentences concise
- Use tables for structured information
- Include checkpoints after key steps
- Use images for architecture (store in `docs/docs/images/`)

### Don't
- Mention costs or pricing
- Use negative framing ("prevents errors", "avoids failures")
- Use sensitive scenarios (healthcare, etc.)
- Include features that can't be implemented in the lab
- Make titles too long (header bar truncates)

## Sample Data Generation

Include a script that generates both:
- **Unstructured data** (PDFs, docs) for document-based products
- **Structured data** (CSV) for data-based products

Provide 5 industry scenarios (avoid healthcare):
1. Retail (recommended default)
2. Hospitality
3. Financial Services
4. Manufacturing
5. Education

Keep default data sizes small for fast execution:
- Documents: 2
- Records: 10-15 per entity

Allow scaling via environment variables.

## Cleanup Module

Always include:
- `azd down` command
- Verification steps
- Congratulations section with accomplishment checklist
- Links to continue learning

## Custom Styling

If title is too long, add `docs/docs/stylesheets/extra.css`:
```css
.md-header__title {
  font-size: 0.8rem;
}
```

Reference in `mkdocs.yml`:
```yaml
extra_css:
  - stylesheets/extra.css
```

## Before Publishing Checklist

- [ ] GitHub Pages enabled (Settings → Pages → GitHub Actions)
- [ ] All modules have overview and step pages
- [ ] Sample data generator works for all scenarios
- [ ] Scripts are numbered in execution order
- [ ] No cost mentions
- [ ] No sensitive industry scenarios
- [ ] Positive language throughout
- [ ] Images in `docs/docs/images/` folder
- [ ] Checkpoints after major steps
- [ ] Cleanup instructions included
- [ ] Title fits in header bar
