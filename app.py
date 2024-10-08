from flask import Flask, render_template, request
from emotion import analyze_sentiment_from_microphone

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_audio():
    # Call the function from emotion.py to analyze audio from the microphone
    text, sentiment_scores = analyze_sentiment_from_microphone()

    if text is None:
        return "Could not recognize the speech."

    # Prepare sentiment score output for user-friendly display in a card format
    sentiment_output = f"""
    <strong>Converted Text:</strong> {text}<br>
    <strong>Sentiment Analysis:</strong><br>
    Positive: {sentiment_scores['pos']*100:.2f}%<br>
    Neutral: {sentiment_scores['neu']*100:.2f}%<br>
    Negative: {sentiment_scores['neg']*100:.2f}%<br>
    <strong>Overall Sentiment:</strong> {'😊 Positive' if sentiment_scores['compound'] >= 0.05 else '😠 Negative' if sentiment_scores['compound'] <= -0.05 else '😐 Neutral'}
    """
    
    return sentiment_output

if __name__ == '__main__':
    app.run(debug=True)
