import random

def hangman():
    words = ['python', 'hangman', 'codealpha', 'internship', 'project']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed))

    while attempts > 0 and '_' in guessed:
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed[idx] = guess
            print("Correct! ", " ".join(guessed))
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
            print("Word: ", " ".join(guessed))

    if '_' not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("❌ Out of attempts! The word was:", word)

if __name__ == "__main__":
    hangman()
