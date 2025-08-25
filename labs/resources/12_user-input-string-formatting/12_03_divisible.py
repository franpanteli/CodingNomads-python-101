# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

number = int(input("Type a number between 1 and 1,000,000 - with no commas: "))
if (number % 3) == 0:
    print("That's divisible by 3")
else:
    print("That's not divisible by 3")

