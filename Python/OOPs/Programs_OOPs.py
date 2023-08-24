#WAP to count the number of objects in a class
'''
class emp:
    cnt=0
    def __init__(self):
        emp.cnt+=1
    
obj1 = emp()
obj2 = emp()
obj3 = emp()
print("Number of objects: ",emp.cnt)
'''

# same question with loop input from user
'''
class emp:
    cnt=0
    def __init__(self):
        emp.cnt+=1
n=int(input("Enter the no. of inputs: "))
for i in range (n):
    i=emp()
print("Number of objects: ",emp.cnt)
'''

# WAP to define a class recatngle with attribute width and height.
# Implement a method called calculate_area that returns its dimensions
# and then prints the area.
'''
class rectangle:
    
    def __init__(self,lenth,breadth):
        self.length=length
        self.breadth=breadth
    def calculate(self):
        return self.length*self.breadth
length=int(input("Enter Length: "))
breadth=int(input("Enter Breaadth: "))
obj=rectangle(length,breadth)
print("Area is: ",obj.calculate())
'''

# WAP to find the area and find perimeter of circle using classes
'''
class circle:
    
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (self.radius**2)*3.14
    def perimeter(self):
        return self.radius*2*3.14
radius=int(input("Enter radius: "))
obj=circle(radius)
print("Perimeter is: ",obj.perimeter())
print("Area is: ",obj.area())
'''

# WAP to create  bank acc with attributes acc_no and balance
# implement two methods for depositing and withdrawing moneyand also
# update the balance
# create an objectwith some transactions and print the before and
# after balance in the account
# take user input: balance; withdraw; deposit
'''
class bank:
    
    def __init__(self,balance,acc_num):
        self.acc_num=acc_num
        self.balance=balance
        self.withdraw=withdraw
        self.depo=depo
    
    def Depo(self,amount):
        return (self.balance+self.amount)
    
    def Withdraw(self,amount):
        if self.balance >= amount:
            self.balance=self.balance-amount
        else:
            print("Insufficient funds")
            exit()

acc_num=int(input("Enter Accountnumber: "))    
balance=int(input("Enter current balance: "))
withdraw=int(input("Enter withdraw amout: "))
depo=int(input("Enter depositing amount: "))
obj = bank(acc_num,balance)
obj.Withdraw(withdraw)
obj.Depo(depo)

print("Final balance: ",obj.balance)
'''

# WAP to define a class calculator with methods for addition, subtraction, multiplication and division
# Use init to initializ numbers from from
# create an object and perform all the above operations
'''
class Operation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def multi(self):
        return self.num1*self.num2
    def div(self):
        return self.num1//self.num2


num1=int(input("enter num 1:"))
num2=int(input("enter num 2:"))
obj=Operation(num1,num2)
print(obj.sum(),obj.sub(),obj.multi(),obj.div())
'''

# WAP to prnt all the prime numbers between an interval using
# classes and objects
# create 2 methods, 1 for loop, other for checking the prime
''' need to check once 
class Prime:
    def __init__(self,num1,num2):
        
        self.num1=num1
        self.num2=num2 
    
    def check_prime(self,num):
        for i in range(2,num):
            if num%i==0:
                return False
            return True
        
    def isPrime(self):
        ls=[]
        for j in range(self.num1,self.num2+1):
            if self.check_prime(j):
                ls.append(j)
        return ls
            
num1=int(input("enter num 1:"))
num2=int(input("enter num 2:"))
obj=Prime(num1,num2)    
print(obj.isPrime)       
'''

