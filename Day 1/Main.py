# print("I am Shayan Hassan\nI am Cs Student\nI am learning Machine Learning")

# name="Shayan"
# age=10
# character='A'
# number=12.5
# print("Name: ",name,"\nAge: ",age)
# print(number)

# Student Information

# name = "Shayan"
# age = 20
# university = "UET Peshawar"
# cgpa = 3.75
# is_student = True

# print("Student Information")
# print("Name:", name)
# print("Age:", age)
# print("University:", university)
# print("CGPA:", cgpa)
# print("Is Student:", is_student)

# Product Information

# product_name = "Laptop"
# price = 75000.50
# quantity = 12
# in_stock = True

# print("Product Details")
# print("Product:", product_name)
# print("Price:", price)
# print("Quantity:", quantity)
# print("Available:", in_stock)

# Data Types Practice

# name = "Ali"
# age = 22
# height = 5.9
# is_graduated = False

# print(name, type(name))
# print(age, type(age))
# print(height, type(height))
# print(is_graduated, type(is_graduated))

# num1=10
# num2=10
# avg_number=(num1+num2)/2
# print(avg_number)

# name=(input("Enter Your Name: "))
# print("Hello: ",name)

# print(5=='5')
# print(5 is '5')

# a=5
# b=5

# print(a is b)
# print(a==b)

# name='Shayan'
#  print(type(name))
# name=int(name)
# print(type(name))

# number=22
# number=float(number)
# print(type(number))

# print("Celsius to Fahreheit Converter")
# cel=int(input("Enter Temprature in Celsius: "))
# fah=(cel*(9/5))+32
# print("Temprature in Fahreheit: ",fah)

# number='45'
# number1=int(number)
# print(type(number1))
# number2=float(number)
# print(type(number2))

length=float(input("Enter length: "))
width=float(input("Enter width: "))

area=(length*width)
print("Area: ",area)

sum=0
for i in range(1,11):
    sum+=i
print(sum)

def cal_avg(a,b,c):
    sum=a+b+c
    return sum/3

num1=int(input("Enter Number1: "))
num2=int(input("Enter Number2: "))
num3=int(input("Enter Number3: "))
print("The Avg of three numbers are: ",cal_avg(num1,num2,num3))

avg=lambda a,b: (a+b)/2
print(avg(9,18))


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input("Enter Number: "))
print("The value is: ",factorial(n))

salary=int(input("Enter Your Salary: "))

if salary >0 and salary<30000:
     tax_rate=5
elif salary>30000 and salary<50000:
    tax_rate=15
else:
    tax_rate=15

tax=(salary*tax_rate)/100

final_salary=salary-tax

print("Salary: ",salary)
print("Tax Rate: ",tax_rate)
print("Tax: ",tax)
print("Final Salary: ",final_salary)


import random

secret_number = random.randint(1, 100)

while True:
    guess=int(input("Enter Number: "))
    if guess > secret_number:
        print("High")
    elif guess < secret_number:
        print("Low")
    else:
        print("Correct!...")
        break

