#  Smart Resume Analyzer using Google Gemini AI

A powerful AI-powered web app that evaluates resumes and gives insightful feedback using Google Gemini API. The app extracts text from PDF resumes and provides detailed analysis, skill suggestions, and a score out of 100.

# Features

1. Upload and analyze resumes in PDF format  
2. Extracts text using `pdfplumber` with fallback to OCR (`pytesseract`)  
3. Uses Google Gemini to generate:
      Strengths and weaknesses
      Existing and recommended skills
      Course recommendations
      Resume quality score (0–100)  

4. Clean and responsive UI with Streamlit
5.  Resume score displayed as a progress bar  
6.  Supports Windows and Unix systems  

# Installation & Setup

1. Clone the Repository
     git clone https://github.com/your-username/resume-analyzer.git

# Tech Stack
Python 3
Streamlit – Web app framework
Google Generative AI SDK – Gemini AI responses
pdfplumber – Text extraction from PDF
pytesseract – OCR fallback if needed
pdf2image – Convert PDF pages to images
dotenv – For managing environment variables
