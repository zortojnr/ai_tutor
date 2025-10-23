import os
import sys
from pathlib import Path
from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from utils.gemini_helper import get_math_response
from dotenv import load_dotenv
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

load_dotenv()

# Set up Jinja2 environment
template_dir = Path(__file__).parent.parent / "templates"
env = Environment(loader=FileSystemLoader(template_dir))

def render_template(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = render_template("index.html")
            self.wfile.write(html_content.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            
            question = parsed_data.get('question', [''])[0]
            
            try:
                print(f"Processing question: {question}")
                result = get_math_response(question)
                print(f"AI Response: {result[:100]}...")
                
                if result and result.strip():
                    user_query = {"type": "user", "message": question, "timestamp": datetime.utcnow()}
                    agent_query = {"type": "agent", "message": result, "timestamp": datetime.utcnow()}
                    response = [user_query, agent_query]
                else:
                    print("Empty result from AI")
                    user_query = {"type": "user", "message": question, "timestamp": datetime.utcnow()}
                    error_response = {"type": "agent", "message": "Sorry, I couldn't generate a response. Please try again.", "timestamp": datetime.utcnow()}
                    response = [user_query, error_response]
            except Exception as e:
                print(f"Error in ask_math: {str(e)}")
                user_query = {"type": "user", "message": question, "timestamp": datetime.utcnow()}
                error_response = {"type": "agent", "message": f"Sorry, I encountered an error: {str(e)}", "timestamp": datetime.utcnow()}
                response = [user_query, error_response]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = render_template("index.html", response=response)
            self.wfile.write(html_content.encode())
        else:
            self.send_response(404)
            self.end_headers()
