from abc import ABC,abstractmethod

class Animal:
    @abstractmethod
    def sound(self):
        pass
    
class Lion:
    def sound(self):
        print("Roar")
        
class cat:
    def sound(self):
        print("Mew")
        
lion=Lion()
lion.sound()

catt=cat()
catt.sound()