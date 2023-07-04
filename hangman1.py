import random

def hangman():
    words = ["strawberry", "apple", "banana", "avocado", "orange", "pomegranate", "kiwi", "mango"]
    word = random.choice(words)
    guessed_letters = ""
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess in guessed_letters:
            print("Invalid guess. Please enter a single letter that you haven't guessed before.")
            continue

        guessed_letters += guess

        if guess not in word:
            tries -= 1
            print(f"Wrong guess! Tries remaining: {tries}")
            if tries == 0:
                print("You lost! The word was:", word)
                break

        else:
            print(" ".join([letter if letter in guessed_letters else "_" for letter in word]))

            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word:", word)
                break

hangman()