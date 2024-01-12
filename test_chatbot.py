from chat_session_manager import ChatbotSessionManager

#  Example usage
chatbot = ChatbotSessionManager()
chatbot.get_response("user1", "Hi, chatbot!")
chatbot.get_response("user1", "How's the weather today?")
chatbot.get_response("user2", "Hello, is this customer support?")
chatbot.get_response("user1", "Can you check my account balance?")


# Example usage
message = "I met Lucy in New York last week."
chatbot.get_response('user1', message)