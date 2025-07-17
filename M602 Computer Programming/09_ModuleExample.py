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
# install numpy first   
import numpy as np

# Array with 100 random numbers
someNumbers = np.random.random(100)

print("Some random numbers", someNumbers)

print("Sum", np.sum(someNumbers))
print("Min", np.min(someNumbers))
print("Max", np.max(someNumbers))
print("Mean", np.mean(someNumbers))
print("Median", np.median(someNumbers))

# Get 31 values between 1 and 5, evenly spaced:
print(np.linspace(1,5, num=31))

# Get Values from 0 to 10 with a step size of 0.1
print(np.arange(0, 10, 0.1))

# Some more examples
print(np.pi)
print(np.sqrt(16))

# read csv file 

import csv
with open('noisy-dataA.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(', '.join(row))
# another way to read csv file
import csv

# Open the CSV file
with open('noisy-dataA.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read the header
    header = next(csv_reader)
    
    # Read the rest of the data
    data = [row for row in csv_reader]

# Print the header and first few rows of data
print("Header:", header)
print("First few rows of data:")
for row in data[:5]:
    print(row)
    
        
# read csv file "noisy-dataA.csv" and calculate the mean of the second column
import csv
with open('noisy-dataA.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    sum = 0
    count = 0
    for row in spamreader:
        sum += float(row[1])
        count += 1
    print("Mean", sum/count)
    

# write into csv file
import csv

# Data to be written into the CSV file
data = [
    ['Number1', 'Number2', 'Number3'],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# Open a new CSV file in write mode
with open('numbers.csv', mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)
    
    # Write the data to the CSV file
    csv_writer.writerows(data)

print("Data has been written to numbers.csv")
        
###################################################################################################


# What to try out
#################
# - Create a list of greetings and write a function which randomly greets a
# person with a given name
# - Create a list of numbers and use the random module to shuffle the list
# - Create a list of numbers and use the random module to randomly select
# a number from the list
# - Create a sccript that generate a 100 random password including numbers and chars and save values in CSV file
