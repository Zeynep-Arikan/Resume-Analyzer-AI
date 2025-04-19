import cohere
import os
import re
from vector_store import retrieve_similar_cvs
from langchain.prompts import PromptTemplate

# Cohere istemcisi başlatılıyor
import streamlit as st
co = cohere.Client(st.secrets["COHERE_API_KEY"])


# ✅ CV analiz fonksiyonu (RAG destekli)
def analyze_resume_rag(cv_text, job_title=None):
    # similar_examples = retrieve_similar_cvs(cv_text)
    # context = "\n\n".join(similar_examples)

    # PromptTemplate tanımı
    template = PromptTemplate(
        input_variables=["cv_text", "job_title"],
        template="""
You are a professional HR specialist. Below is a resume that needs to be analyzed.
Also provided are similar resumes from past applicants.


--- CURRENT RESUME ---
{cv_text}

Now analyze the resume above in terms of content, language, and suitability for the position of "{job_title}".  
Provide strengths, weaknesses, and improvement suggestions in bullet points.
"""
    )

    # Prompt'u oluştur
    prompt_text = template.format(cv_text=cv_text, job_title=job_title)

    # LLM çağrısı
    response = co.generate(
        model='command-light',
        prompt=prompt_text,
        max_tokens=600,
        temperature=0.7
    )

    return response.generations[0].text.strip()

def compare_with_job_posting(cv_text: str, job_posting: str, job_title: str) -> str:
    template = PromptTemplate(
        input_variables=["cv_text", "job_posting", "job_title"],
        template="""
You are a professional career consultant and HR expert.

The user is targeting the job title "{job_title}".  
Here is their resume:

--- RESUME ---
{cv_text}

Here is the job posting they want to apply for:

--- JOB POSTING ---
{job_posting}

Compare the resume to the job posting and return a detailed analysis:

1. Overall suitability for the job (0-10 score)
2. Missing skills or requirements
3. Suggested additions or changes to the resume
4. Final summary feedback

Format it clearly with numbered bullet points.
"""
    )

    prompt_text = template.format(cv_text=cv_text, job_posting=job_posting, job_title=job_title)

    response = co.generate(
        model='command-light',
        prompt=prompt_text,
        max_tokens=600,
        temperature=0.7
    )

    return response.generations[0].text.strip()

# TO do list
def generate_todo_list(cv_text: str, job_title: str) -> str:
    template = PromptTemplate(
        input_variables=["cv_text", "job_title"],
        template="""
You are an expert career advisor and HR professional.

A user is aiming for the role of "{job_title}".  
Below is their resume:

{cv_text}

Based on the target role, generate a personalized To-Do List that includes:

- Key skills or tools that are commonly expected for this role but missing in the resume  
- Suggested courses or certifications to fill those gaps (name real platforms or certificates if possible)  
- Practical steps to improve the CV content (e.g., quantify achievements, adjust the summary)
- Limit the list to exactly 5 items.  

Format your answer clearly as a markdown To-Do List using checkboxes like this:
- [ ] Learn X
- [ ] Add Y project
- [ ] Take Z course
"""
    )

    prompt_text = template.format(cv_text=cv_text, job_title=job_title)

    response = co.generate(
        model='command-light',
        prompt=prompt_text,
        max_tokens=500,
        temperature=0.7
    )
    
     # Çıktıyı düzenle
    output = response.generations[0].text.strip()


    # Sadece ilk 5 "checkbox" satırını al
    todo_lines = [line for line in output.splitlines() if line.strip().startswith("- [ ]")]
    trimmed_todo = "\n".join(todo_lines[:5])

    return trimmed_todo 
