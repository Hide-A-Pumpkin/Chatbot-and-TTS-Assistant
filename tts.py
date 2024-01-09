from gtts import gTTS
import os
from playsound import playsound

# In this part, I used gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
class TextToSpeechConverter:
    def speak(self, text, language='en'):
        tts = gTTS(text=text, lang=language)
        tts.save("speech.mp3")
        playsound("speech.mp3")

# Example usage
tts = TextToSpeechConverter()
tts.speak("Hello, I am your virtual assistant.")
