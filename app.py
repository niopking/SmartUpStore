from flask import Flask, jsonify
from g4f.client import Client
import platform
import asyncio

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return "Welcome to the Flask app!"

# Route for the tourist attractions
@app.route('/t')
async def t():
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    client = Client()
    prompt = "Give me 10 tourist attractions within a radius of 5 km from the coordinates 44°46'11.6 N 17°09'15.5 E. Print in attraction format: distance: description"
    
    # Making the asynchronous call
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
