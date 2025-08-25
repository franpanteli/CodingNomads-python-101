# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

string = input("type a string: ") #more python programming please
symbol = input("type a symbol: ") #§
#repalce every m with §

index = 0
return_string = ""
for char in string:
    if char==string[0]:
        return_string += symbol
    else:
        return_string += char
    index += 1
print(return_string) #§ore python progra§§ing please