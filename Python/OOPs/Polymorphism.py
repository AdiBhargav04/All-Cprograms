# POLYMORPHISM:
# Poly means mnay and morphs means form or shape
# Polymorphism means having many forms
# By poymorphism, one task can be performedin different ways

# In programming, polymorphism means same function name used for different ytpes

# Additon operator: It does not have a single usage


# Polymorphism with inheritance:
'''
class Vehicle:
    def __init__(self,wheels):
        self.wheels=wheels
    
    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("car has ",self.wheels,"Wheels")

class Bike(Vehicle):
    def drive(self):
        print("bike has ",self.wheels,"Wheels")  
        
obj1=Car(4) 
obj2=Bike(2)

obj1.drive()
obj2.drive()
'''
# This process is for re-implementing a method in child class


# Polymorphism with function and objects:
# We can cretate a func. that takes different objects as a parameter
'''
class India:
    
    def capital(self):
        print("Capital: Delhi")
    
    def lang(self):
        print("Lang: Hindi")

class USA:
    def capital(self):
        print("Capital: W.D.C")    
    
    def lang(self):
        print("Lang: English")
    
def fun(obj):
    obj.capital()
    obj.lang()

obj1=India()
obj2=USA()

fun(obj1)
fun(obj2)
'''

