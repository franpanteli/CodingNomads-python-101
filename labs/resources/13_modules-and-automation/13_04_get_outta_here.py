# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import sys
while True: #infinite loop
    user_input = input("Give me input: ")
    if user_input == "quit":
        sys.exit() #this exits the program - anything after this won't happen