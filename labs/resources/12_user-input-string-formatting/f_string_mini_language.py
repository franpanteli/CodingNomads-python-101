message = "you move me!"
print(f"{message:>20}") #moves the string 20 spaces across - this is a language which is just used inside f strings (the modern version of them)

#character escaping
message = "The door reads 'Do Not Enter!'"
message = 'The door reads "Do Not Enter!"'
message = "The door reads \"Do Not Enter!\"" #this is the same as character escaping, which is a string in another string
    #escaping a character gets rid of its meaning

# this is displayed out over one line, \ escapes the new line characters
long_str = "check out this very long string that is \
full of wisdom so you should definitely keep \
reading all the way to the end!"

print(long_str)  # Prints in one line

#another example
    #long string is a multiple of many little strings
    #this prints the little strings all in one go
long_str = ("hei there "
            "how are you?"
            " remember that this ends up as one string!")

print(long_str)
