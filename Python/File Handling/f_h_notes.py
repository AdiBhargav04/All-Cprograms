# File Handling
# it means the process of dealing with files like performing 
# operations like reading, writing, deleting files.

# Several programming languages have the concept of file handling an dits implementation
# is little complicated

# but in python, it is easy due to in-built functions

# Python treats files in 2 ways, 
# 1. Text and 2. Binary

# Text files: Each line contains sequence of characters and they form a file
# EOL: Each line in a file is terminated by EOL (End of line) which is generally
# a newline character

#Advantages of FILE HANDLING: 
# 1. Alllows performing operations like reading, writing, deleting files.
# 2. Its easy in python, bcoz python provides user-friendly interface
# 3. Platform independent: file handling can work accross different platforms 

# Disadvantages: 
# 1. Can cause a lot of errors whne the code is not written carefully
# 2. Can caues security risk in case of modifying sensitive or confidential files on system


# First step: opening the files

# open(): 
# it is then key in-built function for file handling
# takes two parameters: filename, mode
# Syntax:
# file=open(filename,mode)

# TYPES OF MODES FOR OPENEING FLES
# 1. "r": Default mode, opens an existing file for reading.
#         displays error when the file does not exist

# 2. "a": opens an existing file for appending. Creates a new file if one doesnt exist
#         it wont overwrite the existing data

# 3. "w": opens an existing file for writing. Creates a new file if one doesnt exist
#         it will overwrite the existing data

# 4. "x": creates a new file. If a file already exists,
#         it will show error

# 5. "t": (Default) for handling file in text mode

# 6. "b": for handling file in binary mode(eg. images)

