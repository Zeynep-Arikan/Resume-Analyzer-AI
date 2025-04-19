# Resume Analyzer AI

AI-powered resume analysis app that helps you match your CV to your target job role, identify missing skills, and get personalized improvement suggestions.

- Resume parsing is handled using LangChain’s PyPDFLoader module to extract clean, structured text from PDF documents.
- Prompt construction is done using LangChain PromptTemplate, allowing modular and maintainable prompt design for multiple use cases like scoring, suggestions, and comparison.
- AI responses are generated via Cohere’s `command-light` model, selected for its low-latency and fluent text generation.
- The system mimics a simplified RAG architecture but without a vector database in the deployed version.
- Responses are formatted clearly using bullet points and headings to enhance readability within the Streamlit interface.
- The frontend is built with Streamlit, offering users a lightweight, responsive interface to upload resumes, define target roles, and receive real-time feedback.

---

## 🚀 Features

- 📄 **Resume Upload** – Supports `.pdf` and `.txt`
- 🎯 **Job Match Scoring** – Compares your resume to target job roles
- 🛠️ **To-Do List Generator** – Suggests missing skills, tools & courses (max 5 items)
- 🧩 **Job Description Comparison** – Checks alignment between your resume and a real job ad

---
## 🔗 [**Live Demo – Click to Try the App**](https://resume-analyzer-with-ai.streamlit.app/)

---
