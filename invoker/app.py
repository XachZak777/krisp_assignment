from flask import Flask, request, jsonify
import redis
import requests
import asyncio
import aiohttp

app = Flask(__name__)

# Setup Redis connection
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

async def fetch_recommendation(session, model_name, viewer_id):
    url = f"http://generator:8080/generator/recommend?modelName={model_name}&viewerId={viewer_id}"
    async with session.post(url) as response:
        return await response.json()

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('userId')
    
    # Check local cache first
    cached_result = cache.get(user_id)
    if cached_result:
        return jsonify({"recommendation": cached_result})
    
    # If not in cache, call runcascade
    result = asyncio.run(runcascade(user_id))
    
    # Save result to Redis cache
    cache.set(user_id, result)
    
    return jsonify({"recommendation": result})

async def runcascade(viewer_id):
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_recommendation(session, "model1", viewer_id),
            fetch_recommendation(session, "model2", viewer_id),
            fetch_recommendation(session, "model3", viewer_id),
            fetch_recommendation(session, "model4", viewer_id),
            fetch_recommendation(session, "model5", viewer_id)
        ]
        results = await asyncio.gather(*tasks)
        return ', '.join([result['result'] for result in results])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)