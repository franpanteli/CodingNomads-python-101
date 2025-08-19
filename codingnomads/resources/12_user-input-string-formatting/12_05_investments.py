# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
investment_amount = float(input("Type an investment amount: "))
interest_rate_in_percentage = float(input("Type the percentage of interest: "))
number_of_years_to_invest = float(input("Type the number of years to invest: "))

interest = investment_amount*((interest_rate_in_percentage/100)**number_of_years_to_invest)
return_value = investment_amount + interest

print(f"The future value of this investment is {return_value}")

