# Teach Me Maths - Vercel Deployment

A math tutoring application that uses Google's Gemini AI to provide step-by-step math solutions.

## Setup for Vercel Deployment

1. **Environment Variables**: Make sure to set your `GEMINI_API_KEY` in Vercel's environment variables section.

2. **Deployment**: The app is configured to work with Vercel's serverless functions. Simply push to your connected Git repository or deploy directly.

## Project Structure

- `api/index.py` - Main serverless function handler
- `templates/index.html` - HTML template with math rendering
- `utils/gemini_helper.py` - Gemini AI integration
- `vercel.json` - Vercel configuration
- `requirements.txt` - Python dependencies

## Features

- Interactive math question interface
- Step-by-step solutions using Gemini AI
- LaTeX math rendering with KaTeX
- Responsive Bootstrap UI
- Error handling for API failures

## Local Development

To run locally, you can use the original `main.py` with FastAPI:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

For Vercel deployment, the `api/index.py` file handles the serverless function.
