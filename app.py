import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
from pdf2image import convert_from_path
import pytesseract
import pdfplumber
import re

# Load environment variables
load_dotenv()

# Configure Google Gemini AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Set Tesseract path (Windows users only)
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        if text.strip():
            return text.strip()
    except Exception as e:
        print(f"Text extraction failed: {e}")

    # Fallback to OCR
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            text += pytesseract.image_to_string(image) + "\n"
    except Exception as e:
        print(f"OCR failed: {e}")
    return text.strip()

# Function to get response from Gemini AI
def analyze_resume(resume_text):
    if not resume_text:
        return {"error": "Resume text is required."}

    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f"""
    You are a professional HR expert with technical knowledge in evaluating resumes for technical and managerial roles.

    Please analyze the following resume and provide:
    - Strengths of the resume
    - Weaknesses or areas to improve
    - Skills the candidate already has
    - Skills they should improve or add
    - Course recommendations to boost their profile
    - A professional **score out of 100** indicating the quality of this resume

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")
st.title("Smart Resume Analyzer")
st.write("Upload your resume to receive AI feedback and a score out of 100.")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully.")
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_text_from_pdf("uploaded_resume.pdf")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            try:
                analysis = analyze_resume(resume_text)

                # Try to extract and show score out of 100
                match = re.search(r'(\d{1,3})\s*/\s*100', analysis)
                score = None
                if match:
                    score = int(match.group(1))
                    if 0 <= score <= 100:
                        st.markdown(f"## Resume Score: **{score} / 100**")
                        st.progress(score)

                st.markdown("###  Detailed Analysis")
                st.write(analysis)

            except Exception as e:
                st.error(f"Error during analysis: {e}")
else:
    st.warning("📎 Please upload a PDF resume to begin.")

# Footer
st.markdown("---")
