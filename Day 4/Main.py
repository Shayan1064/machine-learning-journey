# class Car:
#     name="Honda"
#     color="White"
#     speed=260
    
# car1=Car()
# print(Car.name)
# print(Car.color)
# print("The Speed of car is: ",Car.speed)

# class Student:
#     Uni_Name="University Of Engineering and Technology Peshawar"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.subject = "Python"
#         self.student_class = "Final Year"
#     def get_info(self):
#         print(f"University:{self.Uni_Name}\nName:{self.name}\nAge:{self.age}\nSubject:{self.subject}\nClass:{self.student_class}")
# std1 = Student("Shayan", 23)
# std2 = Student("Noman", 16)

# print(std1.name)
# print(std1.age)
# print(std1.subject)
# print(std1.student_class)

# print()
# print(std1.Uni_Name)
# print(std2.name)
# print(std2.age)
# print(std2.subject)
# print(std2.student_class)

# print("Student Information")
# print()
# std1.get_info()

# class Product:
#     count=0
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Product.count+=1
        
#     def get_info(self):
#         print(f"Name:{self.name}\nPrice:{self.price}")
    
#     @classmethod
#     def get_count(cls):
#         print(f"The Total stock: {cls.count}")
    
#     @staticmethod
#     def get_discount(price,discout):
#         print(f"Discounted Price:{price-(price*discout/100)} ")
    
# p1=Product("Pen",1000)
# p2=Product("Mobile",15000)
# p3=Product("Laptop",34000)

# p1.get_info()
# print()
# p2.get_info()
# print()
# p3.get_info()

# Product.get_count()

# p3.get_discount( p3.price,13)

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, newBalance):
#         self.__balance = newBalance

# account1 = BankAccount("Shayan", 12345)

# account1.set_balance(200000)

# print(f"Name: {account1.name}")
# print(f"Balance: {account1.get_balance()}")