# PDF Master API

## Overview

PDF Master API is a Python-based tool designed to convert PDF documents into audio format. This README provides a concise overview of the modules used and the main functionality of the tool.

## Modules Used

- **PyPDF2**: For extracting text from PDF files.
- **gTTS (Google Text-to-Speech)**: For converting extracted text into audio.
- **os**: For handling file operations.

## Main Functionality

1. **Extract Text from PDF**: Utilizes PyPDF2 to read and extract text from PDF documents.
2. **Convert Text to Audio**: Uses gTTS to convert the extracted text into an audio file.
3. **Save Audio File**: Saves the generated audio file in the desired format and location.

## Usage

1. Place the PDF file in the specified directory.
2. Run the script to convert the PDF to audio.
3. The audio file will be saved in the output directory.

## Example

```python
from PyPDF2 import PdfFileReader
from gtts import gTTS
import os

# Function to convert PDF to audio
def pdf_to_audio(pdf_path, audio_path):
    # Extract text from PDF
    pdf_reader = PdfFileReader(open(pdf_path, 'rb'))
    text = ''
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extract_text()

    # Convert text to audio
    tts = gTTS(text)
    tts.save(audio_path)

# Example usage
pdf_to_audio('example.pdf', 'output.mp3')
```

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact [otienoryan812@gmail.com].
