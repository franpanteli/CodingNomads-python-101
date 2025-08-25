# Hangman game
# The word to guess (hard-coded)
word = "hello"

# Create blanks for each letter in the word
blanks = ["_"] * len(word)

# Number of attempts the user has
tries = 10

# Introduction
print("Welcome to Hangman!")
print(" ".join(blanks)) #This prints out the blanks

# Main game loop
while tries > 0:
    # Ask the user for a letter
    guess = input("Guess a letter: ").lower()

    # Only allow single-letter alphabetic guesses
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue #go back to the top / start

    # If the guess is correct, reveal it in the blanks
    if guess in word:
        for i, c in enumerate(word):
            if c == guess:
                blanks[i] = guess
        print("Correct!")
    else:
        # Wrong guess reduces tries
        tries -= 1
        print(f"Wrong! Attempts left: {tries}")

    # Show the current state of the word
    print(" ".join(blanks))

    # Check if the player has guessed the whole word
    if "_" not in blanks:
        print(f"You win! The word was '{word}'.")
        break
# If the loop ends without winning, player loses
else:
    print(f"You lose! The word was '{word}'.")
