from flask import Flask, jsonify, request
from g4f.client import Client as OpenAI
import asyncio

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    coordinates = request.args.get('coordinates', default="Nista", type=str)
    return coordinates

# Route for the tourist attractions
@app.route('/t')
def t():
    prompt = request.args.get('prompt', default="Nista", type=str)
    client = OpenAI()
    
    response = await asyncio.to_thread(
        client.chat.completions.create,
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({"response": response.choices[0].message.content})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
