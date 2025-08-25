# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
opinion = input("Give me your honest opinion: ")
index = 0
return_string = ""
for i in opinion:
    if index %2==0:
        return_string += i.upper()
    else:
        return_string += i
    index +=1
print(return_string)