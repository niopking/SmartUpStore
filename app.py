from flask import Flask, jsonify
from g4f.client import Client as OpenAI
import platform
import asyncio

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return "Welcome to the Flask app!"

zn# Route for the tourist attractions
@app.route('/t')
def t():
    client = OpenAI()
    prompt = "Give me 10 tourist attractions within a radius of 5 km from the coordinates 44°46'11.6 N 17°09'15.5 E. Print in attraction format: distance: description"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
