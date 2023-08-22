# WAP to append the content of one file to the end of another file
'''
filename1=input("Enter name of the file-1: ")
filename2=input("Enter name of the file-2: ")
with open(filename2,"r") as file2:
    line=file2.readlines()
with open(filename1,"a") as file1:
    print(file1.write(line))
with open(filename1,"r") as file1:
    print(file1.read())
'''
'''
filename1=input("Enter name of the file-1: ")
filename2=input("Enter name of the file-2: ")
file=open(filename1,"r")
lines=file.read()
file.close()

file2=open(filename2,"a")
file2.write("\n")
file2.write(lines)
file.close()

f=open(filename2,"r")
print(f.read())
'''
# "a+" : append and then read

# "r+" : read and write

# "w+" : write and read data

'''
file=open("Adi.txt","w+")     # overwrites the existing data
file.write("i study in silicon insti")
file.seek(0)    # takes you too the desired index
print(file.read())
'''

# seek(0): start reading from the starting of the file to end of the file
# seek(10): start reading from the 10th position of the file to end of the file

# write() : 

#WAP to read chacater by character from a file
'''
filename=input("Enter file name: ")
with open(filename,"r") as file:
    for i in file.read():
        print(i)
'''

#WAP to count the number of character, words, spaces and lines in a file:
'''
filename=input("Enter file name: ")
c=0
s=0
with open(filename,"r") as file:
    content=file.read()
    for i in content:
        if i:
            c+=1
        if i== " ":
            s+=1
    lines=file.readlines()
    w=len(content.split())
print("Spaces: ",s)
print("Characters: ",c)
print("Lines: ",lines)
print("Words: ",w)
'''

#WAP to find the line number in which the given word is present:
'''
filename=input("Enter file name: ")
target_word=input("Enter target word: ")
c=0
with open(filename,"r") as file:
    for line in file:
        c+=1
        if target_word in line:
            print(target_word," is present in line number ",c)
            break
    else:
        print("Not found")
'''
