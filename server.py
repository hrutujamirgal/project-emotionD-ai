from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector 

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
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
