print("🤖 DecodeBot Started!")
print("Type 'bye' to exit.\n")

responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I am DecodeBot.",
    "ai": "Artificial Intelligence helps machines think and learn.",
    "python": "Python is a popular programming language.",
    "help": "Try saying hello, ask my name, or type bye.",
    "bye": "Goodbye! Have a great day!"
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", reply)