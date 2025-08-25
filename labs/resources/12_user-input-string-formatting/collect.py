# user_input = input("Enter a string, and it will print out every second character in this. Go ahead: ") #this is a string

# print(user_input.upper()) #print uppercase input

# print every second letter from the input
# for i in range(1,len(user_input)):
#     if (i+1)%2==0:
#         print(user_input[i])


# to capitalise every second letter of the input string
# user_input = input("Enter a string: ")
# return_string = ""
# for i in range(0,len(user_input)):
#     #i is the index of the string
#     if i ==0:
#         return_string += user_input[0].upper()
#     elif (i%2) != 0:
#         return_string += user_input[i]
#     else:
#         return_string += user_input[i].upper()
# print(return_string)

user_input = input("Enter a number and the result will come out squared: ")
#user_input is a string
user_input = int(user_input)
print(user_input**2)

#you might need to check that the input is actually a number
