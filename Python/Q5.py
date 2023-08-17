ls=[]
n=int(input("Enter number of elements you want: "))
for i in range (n):
    num=int(input("Enter value: "))
    ls.append(num)
print("Original list: ",ls)
def num_removal(ls):
    list2=ls
    rem2=[]
    n1=int(input("no. of values you want to remove: "))
    for i in range (n1):
        a=int(input("Enter value: "))
        rem2.append(a)
        list2.remove(a)
    return rem2,list2
print(num_removal(ls))