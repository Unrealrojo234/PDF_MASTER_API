from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS
import fitz  # PyMuPDF
from gtts import gTTS

app = Flask(__name__)

CORS(app)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}

#Home route
@app.route('/')
def home():
    return "<h1 style='text-align:center;color:rebeccapurple;'>Welcome to the PDF to Audio API</h1>"

# Function to extract text from a PDF
def extract_text_from_pdf(doc):
    #doc = fitz.open(pdf_path)  # Open the PDF
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return  text
                                                                                                                                                               
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = extract_text_from_pdf(doc)
        tts = gTTS(text=text, lang='en')
        audio_filename = file.filename + "_audio.mp3"
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
        tts.save(audio_path)
        return jsonify({"audio": f"{audio_filename}"}), 200
   
    else:
        return jsonify({"error": "File type not allowed"}), 400


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

    