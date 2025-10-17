import random

print("This isn a sample file")
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a program, but I'm doing fine. How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", chatbot_response(user_input))
        break
    print("Chatbot:", chatbot_response(user_input))
