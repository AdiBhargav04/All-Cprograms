#Wap to create a new file, write two statements then close the file
'''
myList=["My name is Aditya\n","I live in Jsr\n"]
file = open("p1.txt","w")
file.writelines(myList)
file.close()

file=open("p1.txt","r")
print(file.read())
'''

# WAP to copy one fle to another file

# WAP to count the number of lines in the text file:
'''
filename = input("Enter file name: ")

numLines = 0
with open(filename, "r") as file:
    for line in file:
        numLines = numLines+1
        
print(numLines) 
'''

# Wap to count no of blank spaces in a text file
'''
filename= input("Enter file name: ")
c=0
with open(filename,"r") as file:
    for line in file:
        words=line.split()
        print(words)
        c = c+len(words)-1
        space = space+c
print(space+1)
'''
#WAP to count the occurance of a word in a text file
'''
filename = input("Enter file name: ")
searchWord = input("Enter word: ")
count=0

with open(filename, "r") as file:
    for line in file:
        words = line.split()
        for i in words:
            if i==searchWord:
                count=count+1
print(count)
'''
# create a new file 
# write two statements
# close the file

"""
file = open("Ravi.txt","r")
file.write("We are learning Python \n")
file.write("Silicon Institute")
file.close()
"""
'''
file = open("Ravi.txt","w")
myList = ["We are learning Python \n", "Silicon Institute"]
file.writelines(myList)
file.close()

'''

