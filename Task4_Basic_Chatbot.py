# ============================================================
#   CodeAlpha Python Internship
#   Task 4: Basic Chatbot
#   Author  : Chaudhary
#   Concepts: if-elif, functions, loops, input/output
# ============================================================


def get_response(user_input: str) -> str:
    """Return a predefined reply based on the user's message."""
    text = user_input.lower().strip()

    # --- Greetings ---
    if text in ["hello", "hi", "hey", "hii", "helo"]:
        return "Hi! How can I help you today?"

    # --- Wellbeing ---
    elif text in ["how are you", "how are you?", "how r u", "how r you"]:
        return "I'm fine, thanks! What about you?"

    elif text in ["good", "i'm good", "i am good", "i'm fine", "im fine",
                  "great", "i'm great", "doing well"]:
        return "That's great to hear! 😊"

    # --- Identity ---
    elif text in ["what is your name", "what's your name", "who are you"]:
        return "I'm SimpleBot — a rule-based chatbot built for CodeAlpha internship."

    elif text in ["who made you", "who created you"]:
        return "I was created as part of the CodeAlpha Python internship project."

    # --- Help ---
    elif text in ["help", "what can you do", "commands"]:
        return (
            "You can say:\n"
            "  • hello / hi / hey\n"
            "  • how are you\n"
            "  • what is your name\n"
            "  • tell me a joke\n"
            "  • bye / quit"
        )

    # --- Fun ---
    elif text in ["tell me a joke", "joke", "say something funny"]:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"

    # --- Farewell ---
    elif text in ["bye", "goodbye", "exit", "quit", "see you", "see ya"]:
        return "Goodbye! Have a great day! 👋"

    # --- Unknown ---
    else:
        return (
            "Hmm, I didn't understand that. "
            "Type 'help' to see what I can respond to."
        )


def main():
    print("=" * 50)
    print("         Welcome to SimpleBot 🤖")
    print("   Type 'help' for options, 'bye' to exit.")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Session ended. Goodbye! 👋")
            break

        if not user_input:
            print("Bot: Please type something!")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # Exit after farewell
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit",
                                           "see you", "see ya"]:
            break


if __name__ == "__main__":
    main()
