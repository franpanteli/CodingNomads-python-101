"""
Trip Cost Calculator
This is a small project to get yourself warmed up and keep training your newly found skills in collecting user input and formatting strings.

Create a Python script that asks a user questions in the command line. The script should follow the outlined specifications.

Specifications
Receive the following arguments from the user:

Kilometers to drive
Liters-per-kilometer usage of the car
Price per liter of fuel
Calculate the cost of the trip and display it to the user in the console. Apply some of the string formatting tricks that you learned about in this course section.
"""

km_to_drive = float(input("How many km are you driving? Type: "))
litres_per_km = float(input("How many litres per km usage of the car are there? Type: "))
price_per_liter = float(input("Type the price per liter of fuel: "))
print(f"The cost of the trip is £{km_to_drive*litres_per_km*price_per_liter}0")