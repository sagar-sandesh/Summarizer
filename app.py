from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from summarizer import summarize_text_from_pdf
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'pdf', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'document' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)

        file = request.files['document']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            file_ext = filename.rsplit('.', 1)[1].lower()
            if file_ext == 'pdf':
                summary = summarize_text_from_pdf(filepath)
            else:
                summary = summarize_text_from_pdf(filepath)

            return render_template('result.html', summary=summary)

        else:
            flash('Allowed file types are pdf, txt', 'danger')
            return redirect(request.url)
    return render_template('index.html')
