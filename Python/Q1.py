def findPos(k, n):
    a = 0
    b = 1
    i = 2
    while i!=0:
        c = a + b
        a = b
        b = c
        if b%k == 0:
            return n*i
        i+=1
    return
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))
p=findPos(k,n)
print("Position of ",n,"th multiple of ",k," in Fibonacci Series is", p)


