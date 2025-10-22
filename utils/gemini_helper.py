import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_math_response(prompt: str) -> str:
    system_prompt = (
        "You are a helpful math tutor. "
        "Solve math questions step-by-step, clearly, using LaTeX (KaTeX syntax) for math formatting "
        "and HTML tags (e.g., <b>, <p>, <br>) for text formatting. "
        "Explain prerequisites if needed before solving."
    )

    # Combine system prompt and user question
    full_prompt = f"{system_prompt}\n\nQuestion: {prompt}"

    # Initialize the Gemini model (choose an appropriate one)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate the response
    response = model.generate_content(full_prompt)

    # Return the text content
    return response.text.strip()

# Example usage
if __name__ == "__main__":
    question = "Solve for x: 2x + 5 = 15"
    print(get_math_response(question))
