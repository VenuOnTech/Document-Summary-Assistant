import google.generativeai as genai

def generate_summary(text, length_preference, api_key):
    """Connects to LLM to generate a summary based on user constraints."""
    if not api_key:
        raise ValueError("API Key missing. Please provide a valid GEMINI_API_KEY.")
    
    try:
        genai.configure(api_key=api_key)
        
        # Using the exact model name authorized for your API key
        model = genai.GenerativeModel('gemini-3.6-flash')
        
        # Map the UI selection to specific LLM instructions
        length_instructions = {
            "Short": "Provide a brief summary in 3 to 5 sentences. Highlight only the core idea.",
            "Medium": "Provide a detailed summary in 2 to 3 paragraphs. Include main ideas and key supporting details.",
            "Long": "Provide a comprehensive, structured summary using bullet points and headings. Capture all essential information and nuances."
        }
        
        instruction = length_instructions.get(length_preference, "Summarize the text.")
        
        prompt = f"""
        You are an expert Document Summary Assistant. 
        Analyze the following extracted text and generate a smart summary.
        
        Format Request: {instruction}
        
        Document Text:
        {text}
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        error_msg = str(e).lower()
        if "429" in error_msg or "quota" in error_msg or "rate limit" in error_msg:
            raise Exception("The AI API is currently rate-limited. Please wait 60 seconds and try again.")
        else:
            raise Exception(f"An unexpected API error occurred: {str(e)}")
