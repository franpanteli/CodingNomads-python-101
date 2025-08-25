# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

x = input("type something to win: ")
if x.lower() == "something": #the lowercase version of x 
    print("you win")
else:
    print("you loose")
    
