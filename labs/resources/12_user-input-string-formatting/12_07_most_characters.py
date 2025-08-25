# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string_one = input("Give me one string, with no spaces: ")
string_two = input("Give me another string, with no spaces: ")
string_three = input("Give me a third string, with no spaces: ")
if len(string_one) > (len(string_two) and len(string_three)):
    print(str(len(string_one))+","+string_one)

if len(string_two) > (len(string_one) and len(string_three)):
    print(str(len(string_two))+",",string_two)

if len(string_three) > (len(string_one) and len(string_two)):
    print(str(len(string_three))+",",string_three)
