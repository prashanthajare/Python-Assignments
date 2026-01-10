# Assignment 3 - Task 1
# Task 1: Calculate Factorial Using a Function
print("Task 1: Calculate Factorial Using a Function")

fact_num = int(input("Enter a number: "))

def factorial(fact_num):
    if fact_num == 1:
        return 1
    else:
        while fact_num > 1:
         return fact_num * factorial(fact_num - 1)

result = factorial(fact_num)
print(f"Factorial of {fact_num} is :{result}")

# Task 2: Using the Math Module for Calculations
"""
Uses the math module to calculate the:
1) Square root of the number
2) Natural logarithm (log base e) of the number
3) Sine of the number (in radians)
"""
import math
print("Task 2: Using the Math Module for Calculations")

number = int(input("Enter a number: "))

sqrt_num = int(math.sqrt(number))
nat_log = math.log(number)
sin_num = nat_log * sqrt_num
print(f"Square root of {number} is :{sqrt_num}")
print(f"Natural logarithm of {number} is :{nat_log}")
print(f"Sine of {number} is :{math.sin(number)}")


