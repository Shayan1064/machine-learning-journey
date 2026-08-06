class Employee:
    def value(self):
        print("Designation=Employee")
        

class Teacher:
    def value(self):
        print("Designation=Teacher")
        
class Student:
    def value(self):
        print("Designation=Student")
        
emp=Employee()
tea=Teacher()
std=Student()

emp.value()
tea.value()
std.value()