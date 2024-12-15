from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json  # Receive JSON data from Flutter
    result = {'message': f"Received {data['name']}"}
    return jsonify(result)  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
