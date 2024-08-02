'''
Define a Flask application that provides a web interface to the emotion detection model.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_dect():
    '''
    Define a function that returns the emotion detection result
    for the input text.
    '''
    # Get the input text from the query parameter.
    text = request.args.get('textToAnalyze')
    # Call the 'sentiment_analyzer' function to get the sentiment analysis result.

    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is " \
           f"'anger': {response['anger']} " \
           f"'disgust': {response['disgust']} " \
           f"'fear': {response['fear']} " \
           f"'joy': {response['joy']} " \
           f"'sadness': {response['sadness']} " \
           f"'dominant_emotion': {response['dominant_emotion']}"

@app.route("/")
def render_index_page():
    '''
    function that renders the index.html page.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    