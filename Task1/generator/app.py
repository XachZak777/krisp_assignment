from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_recommendation():
    data = request.get_json()  # Ensure this line is correct
    model_name = data.get("model_name")
    viewerid = data.get("viewerid")

    if not model_name or not viewerid:
        return "Invalid input", 400

    result = {
        "reason": model_name,
        "result": random.randint(0, 100)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)