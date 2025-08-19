# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

def vowel_counter(input_string = "Hello world"):
    counter = 0
    for i in input_string:
        if i in "aeiou":
            counter +=1
    return counter

input_string = input("Type an input string: ")
print(f"The amount of vowels in this string is: {vowel_counter(input_string)}")

