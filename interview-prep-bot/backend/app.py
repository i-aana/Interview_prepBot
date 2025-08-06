  # Main Flask API
from flask import Flask,request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai

#loading env variables 
load_dotenv()
GEMINI_API_KEY=os.environ.get("GEMINI_API_KEY")

#Configure Gemini

genai.configure(api_key=GEMINI_API_KEY)

#Initialize flask app
app=Flask(__name__)

@app.route('/')
def home():
    return "Interview prep bot is running"

@app.route('/generate',methods=['POST'])
def generate_response():
    data=request.json
    user_input=data.get("question","")

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)

    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)