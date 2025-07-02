# 🧠 Resume Analyzer Web App

The **Resume Analyzer Web App** is a smart, lightweight web application that evaluates how well a candidate’s resume matches a given job description. It uses Natural Language Processing (NLP) to extract and compare keywords, providing a **similarity score**, a list of **missing skills**, and **personalized suggestions** for improvement.

Whether you're a job seeker preparing for an application or a recruiter filtering resumes, this tool offers quick and intelligent insights.

---

## 📌 Key Features

✅ Upload PDF Resume  
✅ Paste Job Description Text  
✅ Intelligent Keyword Extraction using spaCy  
✅ Similarity Score using Cosine Similarity (scikit-learn)  
✅ Missing Skills Highlighter  
✅ Improvement Suggestions (Top 10 missing keywords)  
✅ Clean & User-Friendly Web Interface

---

## 🔧 Technologies Used

| Component           | Library / Tool     |
|--------------------|--------------------|
| Web Framework       | Flask              |
| NLP                 | spaCy (`en_core_web_sm`) |
| Text Vectorization  | scikit-learn (`CountVectorizer`) |
| Similarity Matching | scikit-learn (`cosine_similarity`) |
| PDF Parsing         | pdfminer.six       |
| Frontend Templating | Jinja2 (HTML)      |

---

## 📂 Project Structure

