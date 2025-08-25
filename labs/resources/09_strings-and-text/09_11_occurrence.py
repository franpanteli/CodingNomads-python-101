# Find the index of the first occurrence of the letter `n` in the string.

composer = "Ludvig van Beethoven"

#initialise dummy boolean
a=0

#iterate through variable characters
for i in composer:
    print(i)
    #if that character is an n, print out its index
    #there is only one of these
    if i =="n":
        print(a)
    a=a+1
print(composer[19])
#character 19