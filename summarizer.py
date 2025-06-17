import pdfplumber
from transformers import pipeline

# Initialize summarizer pipeline once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

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
    if filepath.endswith('.txt'):
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = extract_text_from_pdf(filepath)
    text = text.replace('\n', ' ').strip()

    chunks = list(chunk_text(text))
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    # Combine summaries for a final summary
    final_summary = " ".join(summaries)
    return final_summary
