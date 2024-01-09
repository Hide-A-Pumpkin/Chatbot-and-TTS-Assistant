import pyttsx3

class TextToSpeechConverter:
    def __init__(self):
        self.engine = pyttsx3.init()
        # You can adjust the properties like voice, rate, and volume as needed
        # For example: self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Example usage
tts = TextToSpeechConverter()
tts.speak("Hello, I am your virtual assistant.")
