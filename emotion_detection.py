import requests
import json

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None  

    response_json = response.json()

    emotions = response_json.get('emotionPredictions', [{}])[0].get('emotion', {})  

    emotion_scores = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
    }

    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

   
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

