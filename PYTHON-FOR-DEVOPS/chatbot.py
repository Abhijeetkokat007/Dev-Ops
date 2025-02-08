# import google.generativeai as ai

# # API Key
# API_KEY = 'AIzaSyCVFpu2v_05mj0HStVllpNP5dIahRB51'

# #Configure the API
# ai.configure(api_key=API_KEY)

# #Create a new model
# model = ai.GenerativeModel("gemini-pro")
# chat = model.start_chat()


# #Start a conversation
# while True:
# message = input('You: ')
# if message.lower() == 'bye':
# print('Chatbot: Goodbye!')
# break
# response = chat.send_message(message)
# print('Chatbot:', response.text)


import google.generativeai as ai
import os

# API Key (Use environment variable for security)
API_KEY = os.getenv("GEMINI_API_KEY")  # Set this in your environment variables

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Start a conversation
while True:
    try:
        message = input("You: ")
        if message.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chat.send_message(message)
        print("Chatbot:", response.text)
    except Exception as e:
        print("Error:", str(e))
