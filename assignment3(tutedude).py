# Write a Python program that:
#1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

#Write a Python program that:
#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
#o   Square root of the number
#o   Natural logarithm (log base e) of the number
#o   Sine of the number (in radians)
#3.   Displays the calculated results.
""" Task 1 Factorial using Recursion """

def fact_rec(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact_rec(num - 1)
# User Input
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = fact_rec(number)
    print(f"Factorial of {number} is: {result}")

""" Task 2 Python Program to Calculate Square Root, Logarithm, and Sine  """
import math
print("\n----- RESULTS -----")
# Taking input from the user
number = float(input("Enter a number: "))
# Calculating values
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)
# Displaying the  results
print("Square Root :", square_root)
print("Natural Logarithm:", natural_log)
print("Sine:", sine_value)

