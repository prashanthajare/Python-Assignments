# Task 1: Check if a Number is Even or Odd
print("Assignment 2 - 1 : Task 1")
number=int(input("Enter a Number Here:"))

if number%2==0:
    print(f"Given {number} is Even Number")
else:
    print(f"Given {number} is Odd Number")

# Task 2: Sum of Integers from 1 to 50 Using a Loop
print("Assignment 2 - 2 : Task 2")
int_sum=0
for i in range(1,51):
    int_sum+=i

print(f"The sum of numbers from 1 to 51 is :{int_sum}")