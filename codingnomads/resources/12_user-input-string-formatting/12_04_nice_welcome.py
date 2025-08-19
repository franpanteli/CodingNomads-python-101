# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

def first_name_return(example="First Second"):
    boolean = True
    return_string = ""
    for char in example:
        if char == " ":
            boolean = False
            pass
        if (char.isalpha()) and (boolean == True):
            return_string += char
    return return_string

name = input("What's your name? Enter: ")

# if we are only given a first name:
if " " not in name:
    print(f"Welcome, {name}!")

else:
    print(f"Welcome, {first_name_return(name)}!")


