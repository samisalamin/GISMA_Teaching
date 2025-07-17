#!/usr/bin/env python3

"""
Example using the csv library

https://docs.python.org/3/library/csv.html

"""

############################

### 1. Reading a File
#To read the contents of a file, you can use the `open()` function along with the `read()` method.

# Open a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


### 2. Writing to a File
#To write data to a file, you can use the `open()` function with the `write()` method.

# Open a file in write mode
with open('example1.txt', 'w') as file:
    file.write('Hello, world!')

### 3. Appending to a File
#To append data to an existing file, use the `open()` function with the `append` mode.

# Open a file in append mode
with open('example1.txt', 'a') as file:
    file.write('\nAppended text.')

### 4. Reading a File Line by Line
#To read a file line by line, you can use a loop.

# Open a file in read mode
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())


### 5. Using `with` Statement
#The `with` statement is used for resource management and ensures that the file is properly closed after its suite finishes.

### 6. Reading file lines using list comprehension
#To read a file line by line, you can use a loop.
file = open('example.txt', 'r')
lines = [line.strip() for line in file]
file.close()
print(lines)

### 7. Reading CSV Files (Comma-Separated Values)
#To read data from a CSV file, you can use the `csv` module.
#This example is for the next lecture
#skipp this part for now
###############################################

import csv
# Read data from csv file

csvfile = "noisy-dataA.csv" # file must be in the same folder, or you need to set the full path

with open(csvfile, "r") as f:  # Open file
    csvReader = csv.reader(f)   # Treat file as csv file
    for row in csvReader:       # Iterate over all rows
        print(row)              # Print each row completely
        print(row[0])           # Print only first entry (i.e. the time column)


# Write data to csv file

with open("output.csv", "w",  newline='') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["a","b","c"])
    csvWriter.writerow(["d","e","f"])
    csvWriter.writerow([1,2,3])

print("Output written to \"output.csv\"")

