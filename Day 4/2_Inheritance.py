class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()

dog.sound()
dog.bark()

class Father:
    def money(self):
        print("Father has money")

class Mother:
    def love(self):
        print("Mother gives love")

class Child(Father, Mother):
    def work(self):
        print("Child work Hard")

c = Child()

c.money()
c.love()
c.work()

class GrandFather:
    def house(self):
        print("Grandfather's house")

class Father(GrandFather):
    def car(self):
        print("Father's car")

class Son(Father):
    def bike(self):
        print("Son's bike")

s = Son()

s.house()
s.car()
s.bike()

# Single:
# A → B

# Multiple:
# A   B
#  \ /
#   C

# Multilevel:
# A → B → C

# Hierarchical:
#     A
#    / \
#   B   C

# Hybrid:
#     A
#    / \
#   B   C
#    \ /
#     D