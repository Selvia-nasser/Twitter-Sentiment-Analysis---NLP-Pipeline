import requests
import json

print("Testing Sentiment Analysis API...\n")

test_tweets = [
    "I love this! Amazing experience!",
    "Selvia is amazing",
    "Not sure how I feel about this...",
    "@user Great work! #happy",
    "Disappointed and frustrated"
]

for tweet in test_tweets:
    response = requests.post('http://localhost:5000/predict',
                            json={'tweet': tweet})
    result = response.json()
    print(f"Tweet: {tweet}")
    print(f"Sentiment: {result['sentiment']}\n")