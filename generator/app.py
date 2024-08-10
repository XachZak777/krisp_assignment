from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generator/recommend', methods=['POST'])
def generate_recommendation():
    model_name = request.args.get('modelName')
    viewer_id = request.args.get('viewerId')
    random_number = random.randint(0, 1000)
    return jsonify({
        "reason": model_name,
        "result": str(random_number)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)