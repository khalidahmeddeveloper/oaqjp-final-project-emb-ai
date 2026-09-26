"""
Emotion Detection Server

This module runs a Flask-based web application providing endpoints
for emotion detection analysis and serving the front-end user interface.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Receives text from query parameters, analyzes emotional content,
    and returns a formatted string with all emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant = response['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


@app.route("/")
def render_index_page():
    """
    Renders and displays the index.html home page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
