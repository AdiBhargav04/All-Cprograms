ls1 = []
ls2 = []
n=int(input("Enter the size of list: "))
for i in range(n):
    ls1.append(input("Enter the character: "))
for i in range(n):
    ls2.append(int(input("Enter the number: ")))
print("List 1: ",ls1)
print("List 2: ",ls2)
ls= list(set(ls2))
ls.sort()
res = []
for i in ls:
    for j in range(0, len(ls2)):
        if(ls2[j] == i):
            res.append(ls1[j])
print(res)