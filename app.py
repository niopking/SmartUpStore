from flask import Flask

app = Flask(__name__)

@app.route('/')  # This handles GET requests to "/"
def home():
    return "Welcome to my Flask app!"

if __name__ == '__main__':
    app.run()
