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
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

### 3. Appending to a File
#To append data to an existing file, use the `open()` function with the `append` mode.

# Open a file in append mode
with open('example.txt', 'a') as file:
    file.write('\nAppended text.')

### 4. Reading a File Line by Line
#To read a file line by line, you can use a loop.

# Open a file in read mode
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())


### 5. Using `with` Statement
#The `with` statement is used for resource management and ensures that the file is properly closed after its suite finishes.

# Open a file using with statement
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

### 6. Reading CSV Files
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

with open("output.csv", "w") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(["a","b","c"])
    csvWriter.writerow(["d","e","f"])
    csvWriter.writerow([1,2,3])

print("Output written to \"output.csv\"")
