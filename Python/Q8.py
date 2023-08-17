str1=input("Enter string1 : ")
str2=input("Enter string2 : ")
ct=0
res=""
for i in str1 and str2:
    if i in str1 and str2:
        res=res+" "+i
print("No. of matching characters: ",len(res))
print("Matching characters: ",res) 