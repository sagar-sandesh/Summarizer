import pdfplumber
from transformers import pipeline
import torch

device = torch.device('cpu')
# Initialize summarizer pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device =-1)

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def chunk_text(text, max_length=1000):
    # Split text into chunks of max_length tokens approx
    words = text.split()
    for i in range(0, len(words), max_length):
        yield " ".join(words[i:i+max_length])

def summarize_text_from_pdf(filepath):
    import PyPDF2

    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Optionally limit text size for summarizer model
    max_length = 1024  # model-dependent
    input_text = text[:4000]  # truncate if too long

    summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
