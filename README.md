# Document Summary Assistant

**Live Application URL:** [Insert your deployed URL here]

## Approach Write-up
This application uses a decoupled architecture prioritizing maintainability, error handling, and user experience. Built with Streamlit, the frontend offers a responsive, drag-and-drop interface with clear loading states. The backend logic resides in a modular `core/` directory. Text extraction is explicitly routed based on MIME types: `pdfplumber` parses digital PDFs to maintain formatting, while Tesseract OCR processes scanned images. 

For intelligent summarization, the app integrates the Google Gemini AI model. Dynamic prompting allows the user to scale the summary length (Short, Medium, Long) while enforcing key point extraction. To ensure production quality, API keys are managed securely via environment variables with a UI fallback for local testing, and robust error handling is implemented to catch unreadable text or API rate limits gracefully.

## Setup Instructions
1. Clone the repository and navigate to the root directory.
2. Install system dependencies: Tesseract OCR is required for image extraction.
3. Install Python dependencies: `pip install -r requirements.txt`
4. Set your API Key: Rename `.env.example` to `.env` and add your Gemini API key.
5. Run the application: `streamlit run app.py`
