'''
This module contains a function that takes a text as input and returns the emotion of the text.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    This function takes a text as input and returns the emotion of the text.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
    url += 'NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=myobj, timeout=1)
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # get the key from formatted_response['emotion'] with the highest value
    dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'],
                           key=formatted_response['emotionPredictions'][0]['emotion'].get)

    return {
            'anger': anger_score, 
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion,
            }
