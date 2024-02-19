import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3
from textblob import TextBlob


patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I\'m doing well, thanks for asking.']),
    (r'what is your name?', ['I am just an AI chatbot'])
]
chatbot = Chat(patterns, reflections)

engine = pyttsx3.init()

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.5:
        return "It sounds like you're feeling very positive!"
    elif sentiment_score > 0:
        return "It sounds like you're feeling positive!"
    elif sentiment_score < -0.5:
        return "It seems like you're feeling very negative. Is there anything I can do to help?"
    elif sentiment_score < 0:
        return "It seems like you're feeling negative. Is there anything I can do to help?"
    else:
        return "Your sentiment is neutral. How can I assist you further?"


def chat_with_bot_text():
    print("Welcome to the Chatbot. Type your message to interact or type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            speak("Goodbye!")
            break
        else:
            sentiment_response = analyze_sentiment(user_input)
            print("Sentiment Analyzer:", sentiment_response)
            speak(sentiment_response)
            if "negative" in sentiment_response.lower():
                continue_chat = input("Chatbot: Is there anything I can do to help? (yes/no) ")
                if continue_chat.lower() != 'yes':
                    print("Chatbot: Alright, feel free to reach out if you need assistance. Goodbye!")
                    speak("Alright, feel free to reach out if you need assistance. Goodbye!")
                    break
                else:
                    continue
            response = chatbot.respond(user_input)
            print("Chatbot:", response)
            speak(response)


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    chat_with_bot_text()
