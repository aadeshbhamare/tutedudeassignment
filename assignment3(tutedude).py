# Write a Python program that:
#1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

""" Factorial using Recursion """

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

