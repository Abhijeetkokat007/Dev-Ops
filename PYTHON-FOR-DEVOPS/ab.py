import google.generativeai as ai

# Directly setting the API key (Replace with your actual API key)
API_KEY = "AIzaSyDPt_z1OBtkBjtV-1z1Nkt8plmr8krNE1M"  # Replace with your actual API Key

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model instance
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Start a conversation loop
print("Chatbot: Hello! Type 'bye' to exit.")
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
