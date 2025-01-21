# -*- coding: utf-8 -*-
"""
Script 4 Control Flow (Student Version)
Created on Sun Dec 22 04:40:43 2024
@author: HSS
"""
# 4.1 Conditional Statements
#
# 4.1.1 if

# Example 4.1
if True:  # if a boolean value is True
    print("This is where `True` code is run")  # Code inside the block executes
print("code runs after if statement")

# Example 4.2
if False:  # if a boolean value is False
    print("This code will not run")  # Code inside the block does not execute
print("code runs after if statement")

# Example 4.3: Demand-Supply Gap
supply = 1200  # Units supplied
demand = 1500  # Units demanded
if demand > supply:
    print("Market is in a shortage.")  # Executes if demand exceeds supply


# 4.1.2 if-else

# Example 4.4: Temperature Check
temperature = int(input("What is the temperature in Celsius? "))
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's a pleasant day.")  # Executes if temperature is 30 or below
#
#  Note: the input() function collects user input as a string while 
#        the int() function converts the string to an integer.

# Example 4.5: Even or Odd Number
y = 7
if y % 2 == 0:
    print("y is even.")
else:
    print("y is odd.")  # Executes if y is not divisible by 2

# Example 4.6: Budget Feasibility
I = 100  # Consumer's income
P_x = 10
P_y = 5
Q_x = 6
Q_y = 8
E = P_x * Q_x + P_y * Q_y
if E <= I:
    print("The consumption bundle is affordable.")
else:
    print("The consumption bundle exceeds the budget.")

# Example 4.7: Check Group Size
students = int(input("Enter the number of students: "))
group_size = int(input("Enter the group size: "))
# Check if the students can be evenly divided into groups
if students % group_size == 0:
    print(f"The students can be evenly divided into"
          f"{students // group_size} groups.")
else:
    print(f"The students cannot be evenly divided."
          f"You'll have {students // group_size} full groups"
          f"and {students % group_size} students left over.")
# Note: the implicit string concatenation is used as a line continuation 
#       character. It allows us to split a single statement across multiple 
#       lines for better readability.


# 4.1.3 if-elif-else

# Example 4.8: Another Demand-Supply Check
Q_d = 200
Q_s = 200
if Q_d - Q_s > 0:
    print("Demand exceeds Supply - Shortage")
elif Q_d - Q_s == 0:
    print("Demand equals Supply - Equilibrium")
else:
    print("Supply exceeds Demand - Surplus") 

# Example 4.9: Grading System
score = int(input("Enter Your Score (0-100): "))
if score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")  # Executes if score is between 70 and 79
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")  # Executes if score is below 50

# 4.2 Looping Statements
#
# 4.2.1 for-loops

# Example 4.10: Iterating Over a List
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}")

# Example 4.11: Summing Numbers in a Range
total = 0
for i in range(1, 6):  # Iterates from 1 to 5
    total = total + i
    print(total)
print(f"Sum of numbers from 1 to 5: {total}")

# Example 4.12: Using a for-loop with conditions
for i in range(9):
    if i % 2 ==0:
        print(f"{i} is even")

# Example 4.13: Simulating the growth of a bank account over time
# Inputs
initial_balance = 1000  # Initial amount in the account
annual_deposit = 500    # Amount added to the account every year
interest_rate = 0.05    # Annual interest rate
years = 5              # Number of years to simulate
# Initialize balance
balance = initial_balance
# Loop to calculate balance for each year
for year in range(1, years + 1):
    # Add annual deposit
    balance += annual_deposit
    # Apply interest
    balance *= (1 + interest_rate)
    # Print the balance for the year
    print(f"Year {year}: ${balance:.2f}")
        
# 4.2.2 while-loops

# Example 4.14: Counting Down
count = 5
while count > 0:
    print(f"Count: {count}")
    count = count - 1

# Example 4.15: User Input Validation
password = "12345"
user_input = ""
while user_input != password:
    user_input = input("Enter the password: ")
print("Access Granted")

# Example 4.16: Break-even point
p, mc, TFC = 50, 30, 500
q = 0
TR = p*q
TC = TFC + mc*q
while TR < TC:
    q = q+1
    TR = p*q
    TC = TFC + mc*q
print(f"Break-even production level (q): {q} units")

# 4.3 Control Statements

# 4.3.1 break

# Example 4.17: Using break in a for-loop
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)

# Example 4.18: Using break in a while-loop ( to stop the infinite loop)
no_iterations = 0
while True:
    print(no_iterations)
    no_iterations = no_iterations + 1
    if no_iterations == 3:
        break             
# Example 4.19: Searching for an item
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num == 8:
        print("Found 8!")
        break

# 4.3.2 continue

# Example 4.20: Using continue in a for-loop:
for i in range(5):
    if i == 2:
        continue  # Skip the iteration when i equals 2
    print(i)

# Example 4.21: Using continue in a while-loop:
x = 0
while x < 5:
    x = x+1
    if x == 3:
        continue  # Skip printing when x equals 3
    print(x)

# Example 4.22: Filtering specific conditions:
for num in range(5): 
    if num % 2 != 0: 
        continue  # Skip odd numbers
    print(num)