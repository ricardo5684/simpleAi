# Define a dictionary of predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm just a computer program, but I'm doing well! How can I assist you?",
    "bye": "Goodbye! Have a great day!",
    "messi": "Messi is a goat",
    "ronaldo": "Messi is more goat than Ronaldo",
    
    "gord": "gord is a hero in mobile legend which owned Moonton",
    "ronaldo": "Messi is more goat than Ronaldo",
    "ronaldo": "Messi is more goat than Ronaldo",
    "ronaldo": "Messi is more goat than Ronaldo",
    "ronaldo": "Messi is more goat than Ronaldo",
    "ronaldo": "Messi is more goat than Ronaldo",
    "ronaldo": "Messi is more goat than Ronaldo",
    "ronaldo": "Messi is more goat than Ronaldo",
    "default": "I'm sorry, I don't understand that."
}

# Function to get response from the bot
def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    # Get the response from the dictionary, or use the default response if the input is not recognized
    return responses.get(user_input, responses["default"])

# Main conversation loop
print("Bot: Hello! How can I assist you? (Type 'bye' to end the conversation)")

while True:
    # Get user input
    user_input = input("User: ")
    # Get and print bot's response
    bot_response = get_response(user_input)
    print("Bot:", bot_response)
    # Check if the user wants to end the conversation
    if user_input.lower() == "bye":
        break
