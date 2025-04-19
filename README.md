# Resume Analyzer AI

AI-powered resume analysis app that helps you match your CV to your target job role, identify missing skills, and get personalized improvement suggestions.


---

## 🚀 Features

- 📄 **Resume Upload** – Supports `.pdf` and `.txt`
- 🎯 **Job Match Scoring** – Compares your resume to target job roles
- 🛠️ **To-Do List Generator** – Suggests missing skills, tools & courses (max 5 items)
- 🧩 **Job Description Comparison** – Checks alignment between your resume and a real job ad

---
## 🔗 [**Live Demo – Click to Try the App**](https://resume-analyzer-with-ai.streamlit.app/)

---
- Resume parsing is handled using LangChain’s PyPDFLoader for clean and structured text extraction.
- Prompt construction is done using LangChain PromptTemplate, allowing modular and maintainable prompt design.
- AI responses are generated via Cohere’s `command-light` model, selected for its low-latency and fluent text generation.
- Initially planned vector-based retrieval with BERT embeddings and ChromaDB was disabled for cloud compatibility.
- The system mimics a simplified RAG architecture but without a vector database in the deployed version.
