ls=[]
n=int(input("Enter number of elements you want: "))
for i in range(n):
    num=int(input("Enter the value: "))
    ls.append(num)
print("Original list: ",ls)
ls.sort(reverse=True)
print("Sorted list: ",ls)
N=int(input("No. of largest elements you want to print: "))
print(ls[-len(ls):-len(ls)+N])