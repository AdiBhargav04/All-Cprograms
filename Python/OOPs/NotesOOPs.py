# OOPs: Object Oriented Programming
# It is a wy ofprogramming that uses classes and and objects 
# Advantage is : writing reusable codes by creating objects

# main concepts of OOPs in Python:
# 1. Classes
# 2. Objects
# 3. Methods
# 4. Inheeritance
# 5. Polymorphism
# 6. Encapsulation
# 7. Data Abstraction

# what are some real world examples of classes and objeccts
'''
class : car
object 1: A red colour ford, whose speed is 100km/h
object 2: A blue colour Toyota

class : student
object 1: John, Studying CSE
Object 2: Smith, studying Bio            
'''

# What is the need of classes?

# let say you want to track the number of students in a college who have 
# different name and age:

# Thus classes are needed to organize data in a modular way

# How to create a class: 

# using class keyword, then followed by classname
# class  definition syntax:
'''
class classNmae:
    #statement 1:
    .
    .
    .
    #statement N
'''
# for eg:
'''
class Student:
    name = "Aditya"
    age = 20
''' 
# what are attribute?
# Variables that belong to class are called attributes

# how to access attributes of a class

# attributes can be accessed usiing the dot(.) operator. eg: ClassName.attribute
'''
class Student:
    name = "Aditya"
    age = 20
print(student.name) #name
print(student.age) #age
'''

# create Objects: 
# objects are created using constructor(classname())
# syntax: 
'''
obj = className()
print(obj.attributeName)
'''
'''
class student:
    name = "Aditya"
    age = 20
stud1 =student()
print(stud1.name) #name
print(stud1.age) #age
'''

# Methods: functions that belong to a class,
#          functions defined within a class.

# create a method that returns, whether a student is studying or not
'''
class student:
    name = "Aditya"
    age = 20
    
    # methods
    def isStudying(): # passing self parameter her will avoid the TypeError
        return True
stud1 = student()
print(stud1.name) #name
print(stud1.age) #age
print(stud1.isStudying()) # TypeError
'''

# Definition of classes: 
# Class is a collection of objects
# class contains specific attributes(properties) and methods(functions)
# Class contains user-defined blueprints or prototype from which objects are created.

# Empty class:
'''
class Stud:
    pass
'''

# Definition of objects:
# An object is an instance of a class'# The object has its
# own state(variables/attributes) and behaviour(methods(member functions))
# An object contains:
# 1. State: represented by the attributes of an object(properties of object)
# 2. Behaviour: Represented by the methods of an objects
# 3. Identity: unique name given to the obect interact with other objects
'''
for eg 

'''

# Self Parameter: 
# It represents the specified objects of the class
# it is used to access the attributes and methods of the class
# it binds attributes with the given arguments
# self is used within the methods to refer the object itself
# self parameter is not recieved automatically rather passes explicitly, when the method is called

# it a good convention to name it as self, but can use anything apart

# What is constructor?
'''
A constructor is a special type of method which is automatically
called every tiime an object is created.
It is used to initialize the members of the class or objects state
Like methods, constructor can contain a collection of statements 
that are executed only when called
'''
# Creating a constructor in python

#__init__ method:
# IN python, the constructor isa method named __init__ that gets
# called when an object(instance) is created
# This __int__ method is similar to constructors in c++ n java
# used to initialize the attributes of object
# self represents specified instances or objects that binds the attributes and given arguments

'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
stud1 = Student("Adi",20)
stud2 = Student("Darshan",20)
stud3 = Student("Malay",20)
stud1.display()
stud2.display()
stud3.display()
'''

# Default constructor: When we dont include or declare
# constructor in the class it does not perform any task, 
# Only initializes the attributes
'''
class Student:
    name= "Aditya"
    age= 20
    stream= "ECE"
    
    def display(self):
        print("my name is ",self.name)
stud1 = Student()
stud1.display()    
'''

'''
class Employee:
    def __init__(self,name,company,id):
        self.name=name
        self.company=company
        self.id=id
    def display(self):
        print("Name: ",self.name)
        print("Company: ",self.company)
        print("ID: ",self.id)
obj=Employee("Aditya","Silicon",2256)
obj.display(self)
'''

# self: it is a pointer to current object
# The self parameter always points to the current object
# When you are creating an instance of a class, you are creating 
# an object with its own set of attributes and methods

# id(): prints the memory address

# Doc Strings: classes can have documentation strings also called doc strings

# its a string literal that is the first statement in a class used to
# provide documentation and information about the purpose, usage
# or behaviour of class
'''
class DocString():
    """
    example
    """ 
    def __init__(self):
        pass
    def display(self):
        """
        this is a display function
        """
        
print(DocSring.__doc__)
obj=DocString()
print(obj.display().__doc__)
'''

# Instance variables: 
# are specific to the current instance of the class
# specified using self argument




# Class Variables(class attributes):
# can be accessed through the use of class name
'''
class Person:
    count = 0    #class variable
    
    def __init__(self):
        Person.count += 1
        print(Person.count)

print(Person.count)
obj1 = Person()
obj2 = Person()
obj3 = Person()
print(Person.count)
'''
'''
# Instance Variables:
# Are specific to the current instance of the class
# Specified using the self-agrument

class Person:
    
    def __init__(self, name):
        self.name = name        # instance variable , Ravi, Darshan
        
obj = Person("Ravi")  # Ravi
print(obj.name)

obj2 = Person("Darshan")  # Darshan
print(obj2.name)
'''
# Diff between Class and Instance Variables

# 1. Instance variables data are unique to each instance or object of the class
# 1. Class variables are shared by all instances of the class

# 2. Instance variables are variables whose value is assigned inside a constructor or method with self argument
# 2. Class  variables are variables whose value is assigned in the class.


# Ways of declaring class:

# new and modern way. Most preferred and widely used
# python 3
"""
class Car:
    pass
"""

# Also correct but old way
# used in python 2
"""
class Car():
    pass
"""
"""
class Car:
    
    name = "Mercedes"   # class attribute
    
    def drive(self):
        print(" I am driving "+self.name)
        
obj =  Car()
obj.drive()  # I am driving Merecedes

obj2 = Car()
obj2.name = "BMW"  
obj2.drive() # I am driving BMW

obj3 =  Car()
obj.drive()  # I am driving Merecedes
"""



