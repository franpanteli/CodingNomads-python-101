# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

# 1) Convert an int to a float
integer_example = 6
print("integer_example: ", integer_example)
print("type(integer_example): ",type(integer_example))

integer_example = float(integer_example)
print("integer_example: ", integer_example)
print("type(integer_example): ",type(integer_example))

# 2) Convert a float to an int
float_example =7.0
print("float_example: ", float_example)
print("type(float_example): ",type(float_example))

float_example = int(float_example)
print("float_example: ", float_example)
print("type(float_example): ",type(float_example))

# 3) Perform division using a float and an int
float_example =float(float_example)
integer_example=int(integer_example)
print("float_example/integer_example: ", float_example/integer_example)

# 4) Use two variables to perform a multiplication
print("float_example*integer_example: ", float_example*integer_example)
