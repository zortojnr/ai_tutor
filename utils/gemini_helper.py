import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_math_response(prompt: str) -> str:
    try:
        system_prompt = (
            "You are a helpful math tutor. "
            "Solve math questions step-by-step, clearly, using LaTeX (KaTeX syntax) for math formatting "
            "and HTML tags (e.g., <b>, <p>, <br>) for text formatting. "
            "Explain prerequisites if needed before solving."
        )

        # Combine system prompt and user question
        full_prompt = f"{system_prompt}\n\nQuestion: {prompt}"

        # Initialize the Gemini model (choose an appropriate one)
        model = genai.GenerativeModel("gemini-1.5-flash-002")

        # Generate the response
        response = model.generate_content(full_prompt)

        # Return the text content
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error: {str(e)}")
        # Try with a different model if the first one fails
        try:
            model = genai.GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e2:
            print(f"Gemini API Error with fallback model: {str(e2)}")
            return f"Sorry, I'm having trouble connecting to the AI service. Please try again later. Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    question = "Solve for x: 2x + 5 = 15"
    print(get_math_response(question))
