import threading
import spacy
from gtts import gTTS
import os
from playsound import playsound


class ChatbotSessionManager:
    def __init__(self):
        self.sessions = {}  # Dictionary to hold user sessions, use user_id as unique identifier to differentiate between users.
        self.lock = threading.Lock()  # Lock for thread-safe operations
        self.last_active_user = None  # Track the last active user
        # Load the spaCy model for ner
        self.nlp = spacy.load("en_core_web_sm")

    def get_response(self, user_id, message):
        """ Handle the response for a user message."""
        with self.lock:
            # Check if a new conversation is starting or switching back to a previous user
            if user_id not in self.sessions:
                self.create_new_session(user_id)
                print(f"\nConversation with {user_id}:")
            elif self.last_active_user != user_id:
                print(f"\nBack to {user_id}:")

            # Update the last active user
            self.last_active_user = user_id

            # Retrieve or create a new session for the user
            session = self.sessions[user_id]

            # Generate a response
            response = self.extract_entities_and_respond(message)

            # save the conversation history     
            self.save_conversation(session, message, response)

            print(f"{user_id}: {message}")
            print(f"Chatbot: {response}")
            
            # speak out the response
            self.tts_speak(response)
            return response
    
    def tts_speak(self, text, language = 'en'):
        """Convert text to speech using gTTS and play the sound."""
        fp = 'speech.mp3'
        tts = gTTS(text = text, lang = language)
        tts.save(fp)
        playsound(fp)
        os.remove(fp)


    def create_new_session(self, user_id):
        """Initialize a new conversation session for a new user."""
        self.sessions[user_id] = {
            "conversation_history": []
        }

    def save_conversation(self, session, message, response):
        """Save the user message and chatbot response to the conversation history."""
        session["conversation_history"].append({'message':message, 'response':response})
        return response

    def extract_entities_and_respond(self, message):
        """Extract named entities from the message and generate a response."""
        doc = self.nlp(message)

        # Extract entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Generate a personalized response
        response = self.generate_personalized_response(entities)

        return response

    def generate_personalized_response(self, entities):
        """Generate a personalized response based on identified entities."""
        if not entities:
            return "I didn't catch any specific details. Could you tell me more?"

        response = "I notice you mentioned "
        entity_descriptions = []

        for text, type in entities:
            if type == "PERSON":
                entity_descriptions.append(f"a person named {text}")
            elif type == "GPE":
                entity_descriptions.append(f"a place called {text}")
            elif type == "DATE":
                entity_descriptions.append(f"a date called {text}")

        response += ", ".join(entity_descriptions)

        return response



if __name__=='__main__':
    # Initialize and start the chatbot in a terminal-based interface.
    chatbot = ChatbotSessionManager()
    print('Welcome to Chatbot!')
    while True:
        user_id = input("Enter user ID: ")
        if user_id.lower() == 'exit':
            break
        message = input("Enter your message: ")
        if message.lower() == 'exit':
            break

        chatbot.get_response(user_id, message)
