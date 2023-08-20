#Two modes : 

# 1. "a": append at the end of file
# 2. "w": overwrite the entire file

#write()
'''
file=open("Adi.txt","a")
file.write("I am Iron 2 in valo")
file.close()

# open and reading after appending
file=open("Adi.txt","r")
print(file.read())
'''

# "w": overwrites the entire file

file=open("Adi.txt","w")
file.write("I am Iron 2 in valo")
file.close()
# open and reading file
file=open("Adi.txt","r")
print(file.read())

