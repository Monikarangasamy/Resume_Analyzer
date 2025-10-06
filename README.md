
# Smart Resume Analyzer 🧠

A web application built with **Streamlit** and **Google's Gemini AI** that helps you analyze and improve your resume. This tool evaluates your resume, provides a professional score, and offers detailed feedback on strengths, weaknesses, and skill recommendations to enhance your career profile.

-----

## Installation

### Prerequisites

  * Python 3.7+
  * A Google API Key for Gemini AI

### Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/smart-resume-analyzer.git
    cd smart-resume-analyzer
    ```
2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: The `requirements.txt` file is not in the source tree, but the dependencies can be inferred from the `app.py` script.*
4.  **Configure your Google API Key**:
    Create a file named `.env` in the root directory and add your Google API key:
    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```
5.  **Tesseract OCR Setup (Windows only)**:
    If you're using Windows, you must install **Tesseract OCR**.
      - Download and install it from the [Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).
      - Ensure the installation path in `app.py` is correct:
        ```python
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        ```

-----

## Usage

1.  **Run the application**:
    From your terminal, execute the Streamlit application:
    ```bash
    streamlit run app.py
    ```
2.  **Access the web app**:
    Your browser will automatically open the application at `http://localhost:8501`.
3.  **Upload your resume**:
    Click the "Browse files" button and upload a PDF file of your resume.
4.  **Analyze**:
    Click the "Analyze Resume" button. The application will process your resume, and the AI-powered analysis will appear on the screen, including a professional score and detailed feedback.

-----

## Features ✨

  * **AI-Powered Analysis**: Utilizes Google's Gemini AI to provide expert feedback.
  * **Resume Scoring**: Generates a professional score out of 100 to quickly gauge resume quality.
  * **Comprehensive Feedback**: Provides insights into strengths, weaknesses, and areas for improvement.
  * **Skill Recommendations**: Suggests skills to acquire and courses to boost your profile.
  * **Dual-Layer PDF Processing**: Uses `pdfplumber` for structured text extraction and falls back to `pytesseract` (OCR) for scanned PDFs or image-based resumes.
  * **User-Friendly Interface**: A simple and intuitive web interface built with Streamlit.

-----

## Project Structure

```
.
├── .env                  # Environment file for API keys
├── app.py                # Main Streamlit application script
└── output/               # Placeholder for any output files
```

-----

## Dependencies

  * `streamlit`: The framework for building the web application.
  * `google-generativeai`: The official Python SDK for interacting with Google's Gemini AI.
  * `python-dotenv`: To manage environment variables.
  * `Pillow` (`PIL`): The Python Imaging Library, used for image manipulation.
  * `pdf2image`: Converts PDF pages to images.
  * `pytesseract`: A Python wrapper for Google's Tesseract-OCR.
  * `pdfplumber`: Extracts structured text from PDFs.

*Note: It's highly recommended to install these via a `requirements.txt` file.*

-----

## Contribution Guidelines

Contributions are welcome\! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature (`git checkout -b feature/your-feature-name`).
3.  Commit your changes (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Create a new Pull Request.

-----

## License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.
