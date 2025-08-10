# 🎯 Basic Rule-Based Chatbot

def chatbot():
    print("\n🤖 Chatbot: Hello! I'm your friendly chatbot.")
    print("Type 'bye' to end the chat.\n")

    while True:
        # Get user input and normalize it to lowercase
        user_input = input("You: ").strip().lower()

        # Match responses
        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run chatbot
chatbot()
