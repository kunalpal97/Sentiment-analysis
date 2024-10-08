from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

def analyze_sentiment_from_microphone():
    recognizer = sr.Recognizer()

    # Create an instance of the Microphone class
    with sr.Microphone() as source:
        print('Clearing background noise...')
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Waiting for your message...')
        recorded_audio = recognizer.listen(source)
        print('Done recording...')

    try:
        print('Printing the message...')
        text = recognizer.recognize_google(recorded_audio, language='en-US')
        print(f'Your message: {text}')
    except Exception as ex:
        print(ex)
        return None, None

    analyser = SentimentIntensityAnalyzer()
    sentiment_scores = analyser.polarity_scores(text)

    return text, sentiment_scores
