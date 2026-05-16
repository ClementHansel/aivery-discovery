# AVRY Discovery

Architectural Intelligence Platform for the AVRY Neural Engine.

## Overview
AVRY Discovery is a standalone, interactive dashboard designed to provide deep diagnostic visibility into the AVRY project. It mirrors the entire repository and enriches every file with AI-driven architectural insights, functional rationales, and infrastructure analysis.

## Features
- **Neural Visualization**: Interactive force-directed graph of the entire project structure.
- **AI-Injected Source Mirror**: Every file in the `data/vault` contains `// ARCHITECTURE INSIGHT` comments injected by AI.
- **VPS Analysis**: Specialized module for infrastructure bridge and VPS management logic.
- **Test Verification Suite**: List of system tests with links to code and results.
- **Architectural Reports**: Centralized access to system health and performance documents.

## Tech Stack
- **Frontend**: Vanilla HTML5, CSS3 (Premium Dark Mode), Javascript.
- **Visualization**: D3.js (v7).
- **Code Highlighting**: Prism.js.
- **Icons**: Feather Icons.

## Deployment
This project is optimized for static hosting on **Netlify**, **GitHub Pages**, or **Vercel**. 
Simply upload the root directory or push to a GitHub repository.

## Build Process
The dashboard is generated using `build_discovery.py`, which:
1. Walks the original repository.
2. Injects AI rationales as comments into code files.
3. Generates the hierarchical tree and knowledge graph metadata.
4. Categorizes documentation into Reports, Analysis, and VPS modules.

---
© 2026 AVRY Neural Engine Project
