#!/usr/bin/env python3

"""
Examples for functions

https://docs.python.org/3/tutorial/controlflow.html#defining-functions

Sami Alasalamin, 2024, sami.alslamin@gisma.com
"""

# Write a program to create a function that takes two arguments, name and age, and print their value
# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)

##########################

# Print a sentence multiple times, defined by user input

def print_sentence_multiple_times():
    num = int(input("Enter a number: "))
    for _ in range(num):
        print("Hello, GISMA!")
 
 
print_sentence_multiple_times()

##########################


def addNumbers(numberA, numberB):
    """
    Functions should be always documented with such a "Doxygen"-comment
    """
    return numberA + numberB


print("1 + 4 =", addNumbers(1,4))

###########################

def greeting(name="Nobody"):
    """
    Greets the person. Uses "Nobody" if no name is given
    """
    return "Hi " + name + "!"

print("Greeting without argument:", greeting())
print("Greeting with argument:", greeting("John Doe"))

######################
# As you can find in the class slides, create your own library and try to import and reuse the code

# The library 
def calculator_all(a,b):
    return a+b, a-b, a*b, a/b

def hi():
    print("Hello world")
    
if __name__ == "__main__":    
    add, sub, mul, div = calculator_all(7,5)
    print(f"add ={add}, sub = {sub}, mul = {mul}, div = {div}")
    hi()


# Now call

from calculator import calculator_all

def main()-> None:
    print(calculator_all(10,5))
    print(calculator_all(100,10))
    
if __name__ == "__main__":
    main()
    
# What to try out
#################
# - Write a function that asks for the sex and greets accordingly
#- Write a program to create function func1() to accept a variable length of arguments and print their value.
#- Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary
# Write a function called display_student(name, age), tht prints the name and age of the student. Assign a new name show_tudent(name, age) to it and call it using the new name.
# Hint, you can assign the name function into a new name similare to any variable
# Write a function to find the maximum number in a list, without using the max() function
# Hint: you can sort the list and return the correct position (using sort() function), or iterate over all the values and find the max
# Write a Python function that takes a string as input and returns a dictionary containing the number of uppercase and lowercase characters in the string. Any characters that cannot be categorized as uppercase or lowercase (e.g., symbols) should be counted as "other".
# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
# Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list.
