print("This is Day 2")

# ------------------------------
# Check Name
# ------------------------------
name = input("Enter Name: ")
if name == "Sara":
    print("Girl name")
else:
    print("Boy name")

# ------------------------------
# Vote Eligibility
# ------------------------------
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
nation = input("Enter Your Nationality: ")

if age >= 18 and nation == "Pakistan":
    print("You are eligible for Vote\nCast Vote")
else:
    print("You are not eligible")

print("Hello")

# ------------------------------
# Nested Login
# ------------------------------
name = input("Enter User Name: ")
password = input("Enter Password: ")

if name == "Admin":
    if password == "Shayan2115":
        print("Account Login...")
    else:
        print("Password is Incorrect")
else:
    print("Username is Incorrect")

# ------------------------------
# Login Loop
# ------------------------------
while True:
    name = input("Enter User Name: ")
    password = input("Enter Password: ")

    if name == "Shayan" and password == "Shayan2115":
        print("Account Login...")
        break
    elif name == "Shayan":
        print("Password is Incorrect")
    elif password == "Shayan2115":
        print("Username is Incorrect")
    else:
        print("Both username and password are incorrect")

# ------------------------------
# Simple Login
# ------------------------------
name = input("Enter User Name: ")
password = input("Enter Password: ")

if name == "Shayan" and password == "Shayan2115":
    print("Account Login...")
else:
    if name != "Shayan":
        print("Wrong Username")
    else:
        print("Wrong Password")

# ------------------------------
# Countdown
# ------------------------------
i = 5
while i >= 1:
    print(i)
    i -= 1

# ------------------------------
# Multiplication Table
# ------------------------------
number = 1
table = int(input("Enter table: "))

while number <= 10:
    print(table, "*", number, "=", table * number)
    number += 1

# ------------------------------
# Login with Exit
# ------------------------------
CORRECT_USERNAME = "Shayan"
CORRECT_PASSWORD = "Shayan2115"

while True:
    username = input("Enter Username (or type 'no' to exit): ")

    if username.lower() == "no":
        print("Program terminated.")
        break

    password = input("Enter Password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Login successful.")
    elif username == CORRECT_USERNAME:
        print("Incorrect password.")
    elif password == CORRECT_PASSWORD:
        print("Incorrect username.")
    else:
        print("Both username and password are incorrect.")

# ------------------------------
# Area of Rectangle
# ------------------------------
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area:", area)

# ------------------------------
# Sum of 1 to 10
# ------------------------------
total = 0
for i in range(1, 11):
    total += i
print(total)

# ------------------------------
# Average Function
# ------------------------------
def cal_avg(a, b, c):
    total = a + b + c
    return total / 3

num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
num3 = int(input("Enter Number3: "))

print("The Avg of three numbers is:", cal_avg(num1, num2, num3))

# ------------------------------
# Lambda Average
# ------------------------------
avg = lambda a, b: (a + b) / 2
print(avg(9, 18))

# ------------------------------
# Factorial
# ------------------------------
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter Number: "))
print("The value is:", factorial(n))

# ------------------------------
# Salary Tax Calculator
# ------------------------------
salary = int(input("Enter Your Salary: "))

if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

tax = (salary * tax_rate) / 100
final_salary = salary - tax

print("Salary:", salary)
print("Tax Rate:", tax_rate)
print("Tax:", tax)
print("Final Salary:", final_salary)

# ------------------------------
# Number Guessing Game
# ------------------------------
import random

secret_number = random.randint(0, 99)

while True:
    guess = int(input("Enter Number (0-99): "))

    if guess > secret_number:
        print("High")
    elif guess < secret_number:
        print("Low")
    else:
        print("Correct!...")
        break