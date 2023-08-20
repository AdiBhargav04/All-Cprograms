# opening a file
'''
f=open("Adi.txt",r)  # will show eror as the file doesnt exist
'''
# open() func returns a file object which containsread() for reading the contents of file
'''
file = open("Adi.txt","r")
print(file.read())
'''

# If file is located in different folder
'''
file=open("path")
print(file.read())
'''

# using raw strings
'''
file=open("rpath")
print(file.read())
'''

# we use '\\' to dodge the escape sequence error

# by default read() returns the whole text 
# we can specify the number of characters

# returns the first 10 characters
'''
file=open("Adi.txt")
print(file.read(10))
'''

# reading line at a time:
# using readline() func
'''
file=open("Adi.txt","r")
for i in file:
    print(i)
'''

