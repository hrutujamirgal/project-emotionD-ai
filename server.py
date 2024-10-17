"""
This module provides a Flask web server for detecting emotions from text input
using the emotion_detector function from the EmotionDetection package.
It exposes an endpoint that accepts a POST request and returns emotion scores
or an error message if the input is invalid.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handle POST request to detect emotion from the provided text input.
    
    The function expects form data with the key 'text_to_analyze'. If the text is valid,
    it returns the emotion scores and the dominant emotion in JSON format. If the input is invalid
    or empty, it returns an error message.

    Returns:
        A JSON response containing:
            - Emotion scores for 'anger', 'disgust', 'fear', 'joy', and 'sadness'.
            - The dominant emotion.
            - An error message if the input is blank or invalid.
    """
    text_to_analyze = request.form.get('text_to_analyze', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    return jsonify({
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
