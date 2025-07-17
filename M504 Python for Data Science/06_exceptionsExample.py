#!/usr/bin/env python3

"""
Exceptions in Python

How to deal with errors / exceptions like "File not found", "division by zero",
"conversion not possible" etc. in Python and prevent that your program crashes
for example by wrong formatted input files etc.

https://wiki.python.org/moin/HandlingExceptions

Sami Alsalamin, 2024, sami.alsalamin@gisma.com
"""

print(5*"*", "Catch a specific error")
try:
    print(1/0)   # Division by zero not possible -> Exception
except ZeroDivisionError:   # Will catch the ZeroDivisionErrors
    print("Division by Zero catched")
    # Do whatever is necessary to solve the exception

print(5*"*", "Catch a general error")
try:
    print(2/0)   # Again an exception
except:
    print("Something went wrong...")

print(5*"*", "Catch a general error with some more information")
try:
    print(3/0)   # Again an exception
except Exception as e:
    print("Something went wrong and I have the following information:")
    print(e)

# The following line will show what happens if an error is not caught:
# Program will crash...
a = 5/"b"

# ... and the following print will never be executed
print("You will never see this message")


# raise an exception

print(5*"*", "Raise an exception")
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")    

# raise an exception with TypeError classess 
print(5*"*", "Raise an exception with a custom message")
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


# protect the raise exception
print(5*"*", "Raise an exception")
try:
    raise Exception("This is an exception")
except Exception as e:
    print(e)
    

# raise with else and finally 
print(5*"*", "Raise an exception with else and finally")

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause") 
        
divide(10,2)
divide(10,0)        

# custome exception
print(5*"*", "Raise an exception with else and finally")
class MyError(Exception):
    def __init__(self, message):
        self.value = message
    def __str__(self):
        return repr(self.value)
   

try:
    raise MyError("my bad") # constructor!
except MyError as e:
    print('My exception occurred, value:', e)
    
    
# another way to raise a custome exception

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("An error occurred:", str(e))
    
    
# What to try out
#################
# - Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
# hint, use the try and except statement to protect against float conversion error using TypeError or ValueError
# - Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range
# - Write a Python program that prompts the user to input a number and keep printing the input, it handles a KeyboardInterrupt exception if the user cancels the input loop.
# Hint, exception KeyboardInterrupt: Raised when the user hits the interrupt key (normally Control-C or Delete). 
# # During execution, a check for interrupts is made regularly. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.  
# - Write a program to implement a stop watch. The stop watch should start when the user presses the enter key and stop when the user presses the enter key again.
# Hint, use the time.time() function to measure the time when enter pressed first and secnd time and find the difference.
# e.g., elapsed_time = (end_time - start_time)
# - Write a Python program to measure the execution time of a function using the time module.
# Hint, use the time.time() function to measure the time before and after the function execution.
# To get some large time execution, use the time.sleep() function to pause the program for a few seconds. Or use a large loop to make the program run for a longer time.



#################################################################
#Project 

### Project Title: **Interactive Person Data Collection Program**

#### Objective:
The goal of this project is to develop a Python program that allows users to continuously input personal data (name and age) and the date of the input for an infinite number of individuals. 
The program will store this data in a list of 'Person' objects and will handle user interruptions and invalid inputs age <0).

#### Project Description:
Create a Python program that performs the following tasks:
1. **Define a 'Person' Class**:
   - The class should have three attributes: 'name', 'age', 'date'.
   - Implement an '__init__' method to initialize these attributes.
   - Implement an '__str__' method to provide a readable string representation of the object.

2. **Collect User Input**:
   - Continuously prompt the user to enter the name and age of a person.
   - The program reads the system date and clock as the input date when the person data is entered correctly
   - Store each person's data as an instance of the 'Person' class in a list.

3. **Handle Exceptions**:
   - Implement error handling to manage invalid inputs (e.g., non-integer ages, negative ages).
   - Use a 'try-except' block to catch 'ValueError' exceptions and prompt the user to re-enter the data.

4. **Graceful Termination**:
   - Allow the user to stop the input process using a keyboard interrupt (Ctrl+C).
   - Use a 'try-except' block to catch the 'KeyboardInterrupt' exception and terminate the input loop gracefully.

5. **Print a confirmation that a person is correctly added to the list**

6. **Print any message with each iteration, regardless there is a valid input or not**

7. **Display Collected Data**:
   - After the input process is terminated, print the list of all 'Person' objects entered by the user.
