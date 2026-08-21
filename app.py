import os
import streamlit as st
from dotenv import load_dotenv
from core.document_parser import extract_text_from_pdf, extract_text_from_image
from core.llm_summarizer import generate_summary

# Load environment variables for local testing
load_dotenv()

st.set_page_config(page_title="Document Summary Assistant", page_icon="📄", layout="centered")

# --- Sidebar Configuration ---
with st.sidebar:
    st.subheader("⚙️ Configuration")
    # Check for the key in the environment (used in cloud deployments)
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        st.warning("No API key found in environment.")
        api_key = st.text_input("Enter Gemini API Key to continue:", type="password")
        if not api_key:
            st.info("You must provide an API key to generate summaries.")
    else:
        st.success("API Key loaded securely from environment.")
    
    st.divider()
    st.subheader("Summary Settings")
    summary_length = st.radio(
        "Select Length:",
        ("Short", "Medium", "Long"),
        help="Select how detailed the AI summary should be."
    )

# --- Main Interface ---
st.title("📄 Document Summary Assistant")
st.write("Upload a PDF or image to extract text and generate a smart summary.")

uploaded_file = st.file_uploader(
    "Drag and drop your file here", 
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    # Block execution if the user bypassed the sidebar
    if not api_key:
        st.error("Please enter an API Key in the sidebar to proceed.")
        st.stop()
        
    file_type = uploaded_file.type
    file_bytes = uploaded_file.read()
    
    if st.button("Generate Summary", type="primary"):
        with st.spinner("Extracting text and generating summary..."):
            try:
                extracted_text = ""
                if "pdf" in file_type:
                    extracted_text = extract_text_from_pdf(file_bytes)
                elif "image" in file_type:
                    extracted_text = extract_text_from_image(file_bytes)
                
                if not extracted_text:
                    st.error("No text could be extracted. Please ensure the document is readable.")
                else:
                    # Pass the dynamically acquired api_key to the function
                    summary = generate_summary(extracted_text, summary_length, api_key)
                    
                    st.success("Analysis Complete!")
                    st.subheader(f"Results ({summary_length})")
                    st.markdown(summary)
                    
                    with st.expander("View Extracted Raw Text"):
                        st.text(extracted_text)
                        
            except Exception as e:
                st.error(f"Error: {str(e)}")
