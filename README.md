# Resume Analyzer AI

AI-powered resume analysis app that helps you match your CV to your target job role, identify missing skills, and get personalized improvement suggestions.


---

## 🚀 Features

- 📄 **Resume Upload** – Supports `.pdf` and `.txt`
- 🎯 **Job Match Scoring** – Compares your resume to target job roles
- 🛠️ **To-Do List Generator** – Suggests missing skills, tools & courses (max 5 items)
- 🧩 **Job Description Comparison** – Checks alignment between your resume and a real job ad

---
[![Live Demo](https://img.shields.io/badge/🔗 Live_App-Click_to_Run-brightgreen?logo=streamlit)](https://resume-analyzer-with-ai.streamlit.app/)

---

## 📂 Folder Structure
Resume_Analyzer/
│
├── streamlit_app.py              # Ana arayüz (Streamlit)
├── cohere_chain.py               # Cohere & LangChain destekli analiz fonksiyonları
├── vector_store.py               # Vektör veritabanı ile eşleşme (ChromaDB)
├── requirements.txt              # Gereken tüm kütüphaneler
├── README.md                     # Proje açıklaması
├── embedder.py
├── .streamlit/
│   └── secrets.toml              # Cohere API key burada tutulur (yayın için)(henüz yayınlamadım)
│
├── utils/
│   └── pdf_reader.py             # PDF'ten metin çıkaran yardımcı fonksiyon
│


