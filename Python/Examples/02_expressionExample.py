#!/usr/bin/env python3

"""
Examples for basic number handling

https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Sami Alsalamin, 2024, sami.alsalamin@gisma.com 
"""

i = 1       # A integer
f = 2.5     # A float

print("Numbers", i, f)   # Print numbers
print("Add", i+f)        # Add numbers
print("Divide", f/2)
print("i2f:", float(i))          # Convert int to float
print("f2i:", int(f))            # convert float to int
print("round:", int(round(f)))   # Do proper rounding during conversion
print("Modulo", 5%2)             # Modulo operation


"""
Work with strings
"""

s = "This is my string with some meaningful text"

print(s)                     # Print string
print(s.split(" "))          # Separate by spaces
print(s.replace("s", "x"))   # Replace characters
print(s.lower())             # To lower case
print(s.upper())             # To upper case
print(s.find("m"))           # Find a character in the string

# You can access parts of a string (data structure) as follows:
print(s[:4])                 # Print part of the string

# Explanation:
# s[:4]  = All characters till the 4th
# s[1:4] = Character 2 till the 4th (counting starts with 0!)
# s[-4:] = Last four characters
# s[::2] = Every 2nd character

"""
Work with input from user
"""

# Text input
name = input("Please enter your name:")
print("Hi,",name)

# Number input
number = int(input ("Please enter a number:"))
print("Here are your numbers:", list(range(number))) # Print range of numbers

# Check if the input is numeric
number = input("Please enter a number:")
print (number.isdecimal())

"""
Convert between different types

"""
# Note: If the conversion is not possible (for example from float-style string
# to int), you will raise a ValueError.

# We use quotation marks so the numbers are actually strings: You cannot
# perform mathematical operations on it
floatString = "12.3"
intString   = "45"

print("Convert and add 100 to the number")
# with float(<string>) or int(<string>) we convert the string back to a number
print("Convert string", floatString, "to float:", float(floatString)+100)
print("Convert string", intString, "to float:", float(intString)+100)
print("Convert string", intString, "to int:", int(intString)+100)

print("Convert a number to a string")
print("Number:", str(123.54) + str(100))


"""
Work with tuple, set, and list
https://python.land/python-data-types/python-tuple
"""

# unpack trick
a = [1,2,3,4]
b = [5,6,7,8]

c = (a,b)
print (c)
#The leading * operator unpacks the lists into individual elements

c=(*a,*b)
print (c)

# waht is the difference between the two commands?


#Multiple assignment

person = ('Erik', 38, True)
name, age, registered = person

# What to try out
#################
# - How to divide numbers
# - What happens if you divide two integers?
# - How to enter a float and perform calculations with it?
# - How to enter a float and perform calculations with it?
# - How to convert input to integer or float without getting error for unkown type?
# - Read two values and apply all basic math operations 
# - Creat tuple, list, and/or set of ['one', 2, 'three', [1, 2, 3, 4, 5], 5]. What you can creat and what not?
# - Add more items at the end of the created items
# - Remove the second item
# - Replace the second item 
# - delet it again
