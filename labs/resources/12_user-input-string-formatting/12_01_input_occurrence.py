# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

string = input("type a string: ") #hello world
character = input("type a character: ") #o
index = 0
for char in string:
    if string[index]==character:
        print(index)
        break
    index += 1
