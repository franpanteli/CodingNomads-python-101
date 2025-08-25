# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

# import module
import math

# variables
pi = math.pi
r = 3.14 #radius
h = 5 #height

# print volume and surface area
print("volume:", pi*(r**2)*h)
print("surface area:", 2*((pi*r*h)+(pi*(r**2))))