# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49
counter = 0

def row_of_numbers(start):
    start_string = str(start) + " " + str(start+1) + " " + str(start+2) + " " + str(start+3) + " " + str(start+4) + " " + str(start+5) + " " + str(start+6) + " " + str(start+7) + " " + str(start+8) + " " + str(start+9)
    print(start_string)

for i in range(0,50,10):
    row_of_numbers(i)


