"""
Caesar Cipher
Replicate one of the oldest known encryption by writing your own code.

Apply a Caesar cipher of 7 to the secret variable.

P.S.: <http://www.montypython.net/scripts/dentist.php> ;)

You can start with the following code:

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
You can tackle this challenge using the skills you've learned so far in the course. It might take you a moment to figure out a solution, but give it a try.

Some concepts that you've learned about so far that might come in handy are looping, conditional statements, string methods, slicing, and indexing.

As a stretch task you could adapt your solution so that it preserves capitalization of the original text, and that you can change the cipher to get a different encoding.

Can you also write code to reverse the encryption?
"""

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
secret_output = "" #secret shifted fowards by 7

# counter = 0
# for char in lowercase_letters:
#     if (counter -7) < 0:
#         print(char,counter, counter +19)
#     else:
#         print(char,counter, counter -7)
#     counter += 1

#cyphered characters
# a 0 19
# b 1 20
# c 2 21
# d 3 22
# e 4 23
# f 5 24
# g 6 25
# h 7 0
# i 8 1
# j 9 2
# k 10 3
# l 11 4
# m 12 5
# n 13 6
# o 14 7
# p 15 8
# q 16 9
# r 17 10
# s 18 11
# t 19 12
# u 20 13
# v 21 14
# w 22 15
# x 23 16
# y 24 17
# z 25 18
"""_above_
        -> first: index of letter in lowercase_letters
        -> second: index of letter in lowercase_letters which we want to shift it to
    """
# lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

# cyphered_character
def cyphered_character(character):
    if character == "a":
        return "h"
    if character == "b":
        return "i"
    if character == "c":
        return "j"
    if character == "d":
        return "k"
    if character == "e":
        return "l"
    if character == "f":
        return "m"
    if character == "g":
        return "n"
    if character == "h":
        return "o"
    if character == "i":
        return "p"
    if character == "j":
        return "q"
    if character == "k":
        return "r"
    if character == "l":
        return "s"
    if character == "m":
        return "t"
    if character == "n":
        return "u"
    if character == "o":
        return "v"
    if character == "p":
        return "w"
    if character == "q":
        return "x"
    if character == "r":
        return "y"
    if character == "s":
        return "z"
    if character == "t":
        return "a"
    if character == "u":
        return "b"
    if character == "v":
        return "c"
    if character == "w":
        return "d"
    if character == "x":
        return "e"
    if character == "y":
        return "f"
    if character == "z":
        return "g"

    #punctuation and spaces
    if character == ".":
        return "."
    if character == ",":
        return ","
    if character == " ":
        return " "
    """_this function_
        -> takes an input of a character and returns the cyphered character, as a string
    """

#scrambling the message stored in the `secret` variable
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
secret = secret.lower() #makes it lowercase
scrambled_string = "" #string we want to return to populate

for i in secret: #this is the lowercase secret:
    scrambled_string += cyphered_character(i)

print(scrambled_string)