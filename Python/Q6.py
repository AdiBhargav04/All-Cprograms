st=input("Enter a string: ")
ct1=0
ct2=0
ct3=0
for i in st:
    if i.islower():
        ct1+=1
    if i.isupper():
        ct2+=1
    if i==" ":
        ct3+=1
print("No.of lowercase: ",ct1)
print("No.of uppercase: ",ct2)
print("No.of spaces: ",ct3)