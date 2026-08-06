def chatbot():
    print("=" * 50)
    print("        Welcome to CodeAlpha Chatbot")
    print("=" * 50)
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user = input("You: ").strip().lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "hi":
            print("Bot: Hello! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "what is your name":
            print("Bot: I am CodeAlpha Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "thank you":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()