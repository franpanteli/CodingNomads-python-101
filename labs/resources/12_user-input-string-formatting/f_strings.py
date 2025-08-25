#print statements
print("Welcome to the unfulfilling market!")
print("Tell us what you want, and we won't have it.")

#input statements
food = input("What do you want? ")

#asking them for the amount of items which they want 
#the food variable is a string which stores what the user entered
amount = int(input("How much of {0}? ".format(food)))

#printing another statement, they want - then the value of the strings they entered 
print("You want {0} {1}? Sorry, we only have {2}.".format(amount, food, amount-1))
