# Chatbot Assistant

Author: Xinyi Zhao

Date: 1/12/2024

This chatbot application is designed to interact with users through text-based messages and respond with both text and voice using a Text-to-Speech (TTS) system. 
It handles multiple users and maintains separate conversations, while also personalizing responses based on named entity recognition.


## Requirements
Before running the chatbot, make sure you have Python installed on your system. The chatbot requires the following Python libraries:

- spacy: Natural Language Processing library for entity recognition.

- gtts: Google Text-to-Speech, an interface to Google's text-to-speech API.

- playsound: A library to play sound files.

You can install these libraries using pip:

```{bash}
pip install -r requirements.txt
```

## Running the Chatbot
To run the chatbot, use the following command in your terminal:

```{bash}
python chat_session_manager.py
```


## Usage Instructions
1. Start the script in your terminal.

2. When prompted, enter a user ID. This can be any string that uniquely identifies a user (e.g., "user1").

3. Next, enter the message you want to send to the chatbot.

4. The chatbot will process your message and respond both in text and with an audible voice response.

5. To end the chat session, simply close the terminal window or type 'exit'.



## Useful Links

spaCy: https://spacy.io/

gTTS (Google Text-to-Speech): https://pypi.org/project/gTTS/

playsound: https://pypi.org/project/playsound/
