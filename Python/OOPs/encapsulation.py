# Encapsulation
# Process of wrapping of data and the methods within one unit
# It puts restrictions on accessing the variables and methods directly
# and also prevents modification of data

# To prevent accidental change, we can use private variables 

# Aclass is an example of encapsulation as it encapsulates all the data i.e. variables and methods

# inforation hiding

# real life example of encapsulation
# for eg there is a company : dev department, sales department etc
# dev guy want data from sales dept. 
# he cant directly access the data of sales 
# he will have to first contact the manager of sales section and then request 

# Public members, Protected members and private members

# Public members:  Accessible by all
# In a class all the attributes are by default public
"""
class MyClass:
    def __init__(self):
        self.public_attribute = 10
        
    def public_method(self):
        return "It is a public method"
    
obj = MyClass()
print(obj.public_attribute)
print(obj.public_method())
"""

# Protected Members:
# indicated by a single unnderscore prefix
# Although the protected attributes and methods can be accessed
# outside of th class, its a convention to not to access the protected 
# members out of class
'''
class MyClass:
    def __init__(self):
        self._value = 10
        
    def protected_method(self):
        return "It is a protected method"
    
obj = MyClass()
print(obj._value)
print(obj.protected_method())
'''

# Protected members can be accessed or modified in the deerived class
'''
class ParentClass:
    def __init__(self):
        self._value = 10
    def _protectedMethod(self):
        return "Protected method"
    
class Child(ParentClass):
    def __init__(self):
        super().__init__()
        
    def _protected_access(self):
        print(self._value)
        print(self._protectedMethod())
    
    def modify(self):
        self.value = 50
        print("after modification: ",self._value)
        
obj1 = Child()

print(obj1._value)
print(obj1._protectedMethod())

obj2 = Child()

obj2._protected_access()
obj2.modify()
'''

# private members:
# Indicate dusing double underscores
'''
class Vehicle:
    name = "ford"
    __price = "20 lakhs"
print(Vehicle.name)
print(Vehicle.__price)
'''
'''
class Vehicle:
    def __init__(self):
        self.name = "Ford"
        self.__price = "20 lakhs"
        
    def print(self):
        print(self.name)
        print(self.__price)
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        
    def access(self):
        print(self.name)
        print(self.__price)
        
obj1 = Car()
obj1.print()
obj1.access()
'''
# private members are attributes and methods that are intented to be used only wthin the class ther're defined
# they are not meant to accessed or modified directly from oustide the class
# Private members provide a way to encapsulate the internal functionality and data.

# private members can be directly accessed :
'''
class MyClass:
    def __init__(self):
        self.__value = 30
    def ___private_method(self):
        return "private"
    
obj =MyClass()
print(obj._MyClass__value)
print(obj._MyClass___private_method)
'''

# It is not generally recommended to do as it is against the
# principle of encapsulation

 