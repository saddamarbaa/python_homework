
# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        displayed_word = ""

        for character in secret_word:
            if character in guesses:
                displayed_word += character
            else:
                displayed_word += "_"

        print(displayed_word)

        # Return True when every letter has been guessed
        return all(character in guesses for character in secret_word)

    return hangman_closure


# Task 4: Play the Hangman game
secret_word = input("Enter the secret word: ").lower()

hangman = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ").lower()

    if not letter:
        print("Please enter a letter.")
        continue

    if hangman(letter):
        print("Congratulations! You guessed the word!")
        break
