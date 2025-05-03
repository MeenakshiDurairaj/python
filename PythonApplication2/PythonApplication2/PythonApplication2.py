import random

def chatbot_response(user_input):
    greetings = ["hello", "hi", "hey", "greetings"]
    responses = ["Hello! How can I help you?", "Hi there!", "Hey! What's up?"]

    if user_input.lower() in greetings:
        return random.choice(responses)
    else:
        return "I'm still learning! Can you rephrase that?"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))

