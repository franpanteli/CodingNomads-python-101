import random

#the number which they are guessing is a random number
num = random.randint(1, 10)
guess = None

# while the user hasn't guessed the right number
while guess != num:
    #now we have the user's guess and the number which they are trying to
    guess = int(input("guess a number between 1 and 10: "))
    #they guessed it right and the while loop breaks
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        if guess < num:
            print("Your guess is too low")
        if guess > num:
            print("Your guess is too high")

