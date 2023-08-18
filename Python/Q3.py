n=int(input("Enter the size of tuple: "))
ls=[]
for i in range(n):
    ls.append(int(input("Enter the number: ")))
ls.sort()
k=int(input("Enter the value of k: "))
ls1=ls[:k]
ls2=ls[-k:]
res=ls1+ls2
tup=tuple((ls))
print("Input:",tup)
res=tuple((res))
print("Output:",res)