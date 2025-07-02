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
resume-analyzer/
- ├── app.py # Main Flask application with route handling
- ├── analyzer.py # Resume-job description analyzer using NLP
- ├── resume_parser.py # Extracts raw text from uploaded PDF resumes
- ├── templates/
- │ ├── index.html # Upload form and job description input page
- │ └── result.html # Displays similarity score and suggestions
- ├── static/ # (Optional) For custom CSS/JS
- └── requirements.txt # List of required Python libraries


---

## ⚙️ Installation & Setup Instructions

Follow these steps to run the app locally:

----

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer

----
### 2. Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
 
----
### 3. Install the Required Dependencies

pip install -r requirements.txt

----

### 4. Download the spaCy Language Model

python -m spacy download en_core_web_sm

----

### ▶️ Run the App

python app.py

Then open your browser and go to: http://127.0.0.1:5000

----

### 👨‍💻 How It Works

 **1. Upload Resume:** User uploads a PDF version of their resume.

 **2.Job Description Input:** User enters the job description in a textarea form.

 **3.Text Extraction:** The app extracts text from the resume using pdfminer.six.

**4.Keyword Extraction:** spaCy processes both texts and extracts relevant keywords (removing stopwords and punctuation).

**5.Similarity Analysis:** scikit-learn’s CountVectorizer and cosine_similarity compare both keyword sets.

**6.Results:**

 - **Similarity Score:** Percent match between resume and job description.

 - **Missing Skills:** Top skills from the job description that are not found in the resume.

 - **Suggestions:** Actionable suggestions to include specific keywords in the resume.

----

### 💡 Future Enhancements (Ideas)

- Allow uploading of .docx resumes

- Add resume scoring history for users

- User authentication and saving previous analyses

- Visual charts for matching metrics

- Advanced keyword tagging using ML/NER

----
### 📜 License
