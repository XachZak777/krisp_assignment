import requests
import redis
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Initialize Redis
r = redis.Redis(host='redis', port=6379, db=0)

# Local cache with a TTL of 10 seconds
local_cache = {}
cache_ttl = 10
max_cache_size = 3

# Function to fetch data from the generator
def fetch_data_from_generator(model_name, viewerid):
    response = requests.post(f'http://generator:5000/generate', json={"model_name": model_name, "viewerid": viewerid})
    return response.json()

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    viewerid = data.get("viewerid")

    # Check local cache
    if viewerid in local_cache:
        return jsonify(local_cache[viewerid])

    # Check Redis cache if not found in local cache
    cached_data = r.get(viewerid)
    if cached_data:
        return jsonify(eval(cached_data))

    # If no cache, run the cascade
    models = ['model1', 'model2', 'model3', 'model4', 'model5']
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(lambda model: fetch_data_from_generator(model, viewerid), models))

    # Merge results
    merged_results = results

    # Save to local cache with TTL
    if len(local_cache) >= max_cache_size:
        local_cache.pop(next(iter(local_cache)))  # Remove the oldest item

    local_cache[viewerid] = merged_results

    # Save to Redis
    r.setex(viewerid, cache_ttl, str(merged_results))

    return jsonify(merged_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)