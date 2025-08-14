# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:
import random 

guess = input("Type the value of a guess, between 1 and 10: ")
#now the value of their guess is stored in the variable guess

guessing_number = str(random.randint(1, 10))
print(guessing_number)
#this is the package name, followed by the method and its arguments

if guess == guessing_number:
	print("well done, finished")

dummy_boolean = False 
#dummy_boolean is True if the right answer is guessed 

while dummy_boolean == False:
	print("wrong, guess again")
	guess = input("Type the value of a guess, between 1 and 10: ")

	if guess == guessing_number:
		print("well done, finished")
		dummy_boolean = True 

