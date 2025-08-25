# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
number = int(input("Give me a number between 0 and 1,000,000,000, with no commas: "))
number_found = False
while number_found == False:
    for i in range(0,1000000000):
            if i == number:
                print(i)
                number_found = True
                break
