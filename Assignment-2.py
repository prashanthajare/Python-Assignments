# Module 3: Control Structures in Python
# Task 1: Check if a Number is Even or Odd
print("Assignment - 2 : Task 1")
number=int(input("Enter a Number Here:"))
if number%2==0:
    print(f"The Given {number} is Even Number")
else:
    print(f"The Given {number} is Odd Number")

# Task 2: Sum of Integers from 1 to 50 Using a Loop
print("Assignment - 2 : Task 2")
for i in range(1,51):
    print(i)
print("The Sum of Numbers from 1 to 50 is:", sum(range(1,i+1)))
