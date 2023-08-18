import itertools 
st = input("Enter the string: ")

perm = list(itertools.permutations(st))
print("Permuatations of string : ")
for i in perm:
    print("".join(i))