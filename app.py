from flask import Flask
from g4f.client import Client
import platform
import asyncio

app = Flask(__name__)

@app.route('/')  # This handles GET requests to "/"
def home():
    if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    client = Client()
    prompt = "Give me 10 tourist attractions within a radius of 5 km from the coordinates 44°46'11.6 N 17°09'15.5 E. Print in attraction format: distance: description"
    response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run()
