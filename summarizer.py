import pdfplumber
from transformers import pipeline
import torch
from transformers.utils import logging

# Suppress unnecessary logging
logging.set_verbosity_error()

# Force CPU usage
device = torch.device('cpu')

# Initialize summarizer pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text

def chunk_text(text, max_length=1000):
    words = text.split()
    for i in range(0, len(words), max_length):
        yield " ".join(words[i:i+max_length])

def summarize_text_from_pdf(filepath):
    # Use pdfplumber instead of PyPDF2 (better accuracy and consistency)
    text = extract_text_from_pdf(filepath)

    if not text.strip():
        return "No extractable text found in the document."

    chunks = list(chunk_text(text, max_length=1000))
    summaries = []

    for chunk in chunks:
        if len(chunk.strip()) == 0:
            continue
        summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    return "\n\n".join(summaries)