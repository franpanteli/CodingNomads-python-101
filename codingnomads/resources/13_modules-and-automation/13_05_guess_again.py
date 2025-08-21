# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries
# before they lose.
import random
import sys

guess = int(input("Guess a number between 0 and 10: "))
guessing_number = random.randint(0, 10)
number_of_guesses =10
while number_of_guesses > 0:
    number_of_guesses -= 1
    guess = int(input("Guess a number between 0 and 10: "))
    if guess == guessing_number:
        print("You win the game!")
        sys.exit() #this exits the program - anything after this won't happen

print("You lose the game, you didn't guess the number!")