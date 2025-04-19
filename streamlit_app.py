import streamlit as st
from cohere_chain import analyze_resume_rag, compare_with_job_posting, generate_todo_list
# from vector_store import add_cv_to_vector_store
from utils.pdf_reader import extract_text_from_pdf

# Sayfa ayarları
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("AI Resume Analyzer")
st.write("Upload your resume (.pdf or .txt) and get AI-powered feedback!")

# Dosya yükleme
uploaded_file = st.file_uploader("📄 Upload Resume", type=["txt", "pdf"])
job_title = st.text_input("🎯 Target Position (optional)", placeholder="e.g., Frontend Developer")
job_posting = st.text_area("📋 Paste Job Description", height=250, placeholder="Paste job ad from LinkedIn or another site here...")
resume_text = ""


if uploaded_file:
    file_name = uploaded_file.name

    if file_name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(uploaded_file)
    elif file_name.endswith(".txt"):
        resume_text = uploaded_file.read().decode("utf-8")

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing with AI..."):
            # Vektör veritabanına ekleme
            #add_cv_to_vector_store(file_name, resume_text)

            # İngilizce analiz çıktısı
            result = analyze_resume_rag(resume_text, job_title if job_title else None)
            st.success("✅ Analysis Complete!")
            st.markdown("### 📈 English Resume Analysis")
            st.write(result)
        if job_posting.strip():
            st.markdown("### 🧩 Resume vs Job Description Match")
            job_match_analysis = compare_with_job_posting(resume_text, job_posting, job_title)
            st.write(job_match_analysis)
            
            
            # AI destekli geliştirme planı
            st.markdown("### 🛠️ Personalized To-Do List to Improve Your Resume")

            todo_list = generate_todo_list(resume_text, job_title)
            st.markdown(todo_list)
            
