#!/usr/bin/env python3

"""
Examples for loops

https://docs.python.org/3/reference/compound_stmts.html#for
https://docs.python.org/3/reference/compound_stmts.html#while

Sami Alsalamin, 2024, sami.alsalamin@gisma.com
"""

# Print numbers from 1 to 10
print("For loop")
for number in range(1,11):
    print(number)

# Print numbers from 1 to 10 but break loop under certain conditions
print("Break loop")
for number in range(1,11):
    if number == 5:
        break # Stop the loop
    print(number)

# Print numbers from 1 to 10 but continue loop under certain conditions
print("Continue loop")
for number in range(1,11):
    if number % 2: # Modulo operator: %
        continue # Next iteration
    print(number)

# Iterate over items
print("Iterate loop")
items = ["Book", "Banana", "Computer"]
for item in items:
    print("I will take my", item, "with me...")

# While loop
print("While loop")
number = 1
while (number < 10):
    print(number)
    number += 1 # Short form for number = number + 1, number++ does not exist

# What to try out
#################
# 1 - Read a string from the user, and print characters present at an even index number
#  E.g., Hello world, the output (H l o w r d)
# 2 - Write a Python code to remove characters from a string from 0 to n and print the new string
# Hint: Use string slicing to get a substring. For example, remove the first four characters using s[4:]. 
# Protect your execution from wrong input; negative or out of range values.
# 3 - Find the number of occurrences of a substring in a string
# Hint: Use the string method count(). E.g., s.count("something")
# 4 - Write a Python code to check if the given number is a palindrome. A palindrome number is a number that is the same when reversed. For example, 545 is the palindrome number.
# Hint: Reverse the given number and save it in a different variable. Use the if condition to check if the original and reverse numbers are identical. 
# 5 - Given two lists of numbers, write a Python code to create a new list such that the latest list should contain odd numbers from the first list and even numbers from the second list.
# Hints, 
# Create an empty list named result_list
# Iterate the first list using a for loop
# In each iteration, check if the current number is odd using the num % 2 != 0 formula. If the current number is odd, add it to the result list
# Now, iterate the second list using a loop.
# In each iteration, check if the current number is even using the num % 2 == 0 formula. If the current number is even, add it to the result list.
# Print the result list.
# 6 - You can use several loops. Write a program which outputs a multiplication
# table from 1 to 100 (1x1=1, 1x2=2, etc.)
