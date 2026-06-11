# ============================================================
#   CodeAlpha Python Internship
#   Task 1: Hangman Game
#   Concepts: random, while loop, if-else, strings, lists
# ============================================================

import random

# 5 predefined words
WORDS = ["python", "hangman", "laptop", "keyboard", "monitor"]

def display_state(guessed_letters: list, word: str, wrong: int) -> None:
    """Print current hangman figure, word progress, and wrong count."""

    HANGMAN = [
        """
           -----
           |   |
               |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ==========""",
    ]

    print(HANGMAN[wrong])
    print("\nWord: ", end="")
    for letter in word:
        print(letter if letter in guessed_letters else "_", end=" ")
    print()
    print(f"\nWrong guesses left : {6 - wrong}")
    print(f"Letters guessed    : {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")


def hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_count = 0
    max_wrong = 6

    print("=" * 50)
    print("         Welcome to Hangman! 🎮")
    print("=" * 50)
    print(f"  The word has {len(word)} letters. Good luck!\n")

    while wrong_count < max_wrong:
        display_state(guessed_letters, word, wrong_count)

        # Check win
        if all(letter in guessed_letters for letter in word):
            print(f"\n✅ You won! The word was: '{word}'")
            break

        # Get input
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try another.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            wrong_count += 1
            print(f"❌ '{guess}' is NOT in the word!")

    else:
        display_state(guessed_letters, word, wrong_count)
        print(f"\n💀 Game over! The word was: '{word}'")

    print("\n" + "=" * 50)
    play_again = input("Play again? (yes / no): ").lower().strip()
    if play_again in ["yes", "y"]:
        hangman()
    else:
        print("Thanks for playing! Goodbye 👋")


if __name__ == "__main__":
    hangman()
