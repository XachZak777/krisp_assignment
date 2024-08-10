import random
import json
import time
from functools import lru_cache
import redis
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

# Local cache with TTL of 10 seconds and a maximum of 3 keys
@lru_cache(maxsize=3)
def local_cache(viewer_id):
    return redis_client.get(viewer_id)

@app.route('/recommend', methods=['GET'])
def recommend():
    viewer_id = request.args.get('viewer_id')
    cached_result = local_cache(viewer_id)
    if cached_result:
        return jsonify(json.loads(cached_result))

    recommendations = runcascade(viewer_id)
    redis_client.set(viewer_id, json.dumps(recommendations), ex=3600) # Store in Redis with 1 hour TTL
    local_cache.cache_clear() # Clear local cache for new recommendations
    return jsonify(recommendations)

def runcascade(viewer_id):
    results = []
    models = ["model1", "model2", "model3", "model4", "model5"]
    for model in models:
        response = requests.post('http://generator:8000/recommend', json={"model_name": model, "viewer_id": viewer_id})
        results.append(response.json())
    return results

@app.route('/recommend', methods=['POST'])
def generate_recommendation():
    model_name = request.json.get('model_name')
    viewer_id = request.json.get('viewer_id')
    random_number = random.randint(1, 100)
    result = {
        "reason": model_name,
        "result": random_number
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)