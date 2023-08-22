# Exception Handling

# What are errors in programming

# 1. Run-time error : Errors during the execution of the program. eg: division by zero

# 2. Syntax error : Caused due to incorrect syntax which leads to termination of program

# What is an exception?

# Exception is a specific type of run-time error that occurs when 
# program encounters a situation that it cannot handle.

# Different types of exception in python

# 1. TypeError: This exception is raised when an operation is applied to 
#    wrong type

# 2. KeyError: Trying to access any key that is not found in dictionary

# 3. IndexError: Tis exception is raised whn an index is out 
#    of range for a list, tuple etc,.

# 4. ValueError: This eroor is raised when a function is called 
#    with invalid argument or values.

# 5. ZeroDivisionError: This exception is raised when we try
#    to divide a number by zero. 

# How to handle these exceptions? (Runtime)
# Try and except statements: Catching the exceptions
# used to catch and handle the exceptions in python
# statements that can cause excepion are kept in try block
# and the statements that handle the exceptions are kept in 
# Except block

# without try block, program will crash and raise error

# Catching specfic exceptions
# We can declare multiple except block for handliing different exceptions

# Try with else block: 
# Executes only when the try block doesnot raise an exception

# Finally keyword in try Except block:

