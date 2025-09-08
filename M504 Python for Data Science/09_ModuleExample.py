#!/usr/bin/env python3

"""
Examples for random numbers, numpy and csv

https://docs.python.org/3/library/random.html
https://docs.python.org/3/library/csv.html
https://numpy.org/

Prof. Dr. Sami Alsalamin, 2024, sami.alslamin@gisma.com
"""

import random

random.seed(34) # Set the seed for the RNG

sequence = ["Apple", "Pear", "Peach", "Pineapple"]

print("Random integer between 1 and 10:", random.randint(1,10))
print("A random fruit:", random.choice(sequence))
print("A float between 0 and 1:", random.random())
print("Gaussian distribution with mu=0 and sigma=1:", random.gauss(0,1))

print("Items:", sequence)
random.shuffle(sequence)
print("Shuffled items:", sequence)

print("3 random elements out of the sequence:", random.sample(sequence,3))

############
# select a random character from a string
import random

name = 'pynative'
char = random.choice(name)
print("random char is ", char)

# select a random number from a list
import random
numbers = [1, 2, 3, 4, 5]
number = random.choice(numbers)
print("random number is ", number)

#######
# shuffle a list
a =[1,2,3,4,5]
random.shuffle(a)
print(a)
###############################################################################

        
###################################################################################################


# What to try out
#################
# - Create a list of greetings and write a function that randomly greets a
# person with a given name
# - Create a list of numbers and use the random module to shuffle the list
# - Create a list of numbers and use the random module to randomly select
# a number from the list
