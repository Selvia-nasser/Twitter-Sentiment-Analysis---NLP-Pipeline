# TASK 11: FLASK API
from flask import Flask, request, jsonify
import joblib
import re

# Load model
model = joblib.load("X:/Projects/Sentiment Analysis Task/sentiment_model.pkl")

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Sentiment Analysis API', 'status': 'running'})


@app.route('/predict', methods=['POST'])
def predict():
    # Get tweet from request
    data = request.get_json()
    tweet = data.get('tweet', '')

    if not tweet:
        return jsonify({'error': 'No tweet provided'}), 400

    # Clean tweet
    cleaned = re.sub(r'http\S+|www\S+|https\S+', '', tweet)
    cleaned = re.sub(r'@\w+', '', cleaned)
    cleaned = re.sub(r'#', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    # Simple preprocessing - just lowercase (same as what the model expects)
    processed = cleaned.lower()

    # Predict
    prediction = model.predict([processed])[0]

    return jsonify({
        'tweet': tweet,
        'sentiment': prediction,
        'processed_text': processed
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)