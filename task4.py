# basic_chatbot.py

def chatbot():
    print("🤖 Welcome to the Basic Chatbot!")
    print("Type something to begin (type 'exit' to quit):\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! 👋")
            break
        elif user_input in ["hello", "hi"]:
            print("Chatbot: Hi there! 👋")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks for asking! 😊")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Take care! 👋")
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
