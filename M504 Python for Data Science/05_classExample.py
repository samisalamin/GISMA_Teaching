#!/usr/bin/env python3

"""
Examples for Python classes

https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes

Sami Alsalamin, 2024, sami.alsalamin@gisma.com

This example requires the module with the name "myClassExample.py" in the same
directory. It contains the class "helperClass" used in this program.
"""

# check available types in python
def h():
    print("Hello")
    
a = 5.2
b = 'Hello World'
c = [1, 2, 3]
d = False
e = range(4)
f = (1, 2, 3)
g = complex(1, -1)

for var in [a, b, c, d, e, f, g, h]:
    print(var.__class__)
    # OR
    print(type(var))
    
########################
# Your first class
# Static class
class Student:
    name = "Jane"
    course = "JavaScript"

Student1 = Student()
print(Student1.name)
# Jane
     
####################

class Student:
    school = "GISMA.com"

    def __init__(self, name, course):
        self.name = name
        self.course = course

Student1 = Student("Jane", "Java")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John        
    
print(Student1.school)
print(Student2.school)    
###################
# Using __str__

# Try the following
# What print shows?

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# Modify to
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

################
# insert any function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#################
# Do you have to use self keyword always?
# Try 

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

####################
# set a value
p1.age = 40

###################
# delete a property
del p1.age

####################
# delete an object
del p1

#########################################
# Use class as a seperated file
# save the following class into a file , as myClassExample.py

"""
Example Python class

myClassExample 

"""

class helperClass:
    """
    Just a dummy class without a special meaning
    """
    def __init__(self, name="Nobody"):
        """
        The constructor where a name can be set. Default name: "Nobody"
        """
        self.name = name

    def hi(self):
        """ Greeting """
        print("Hi,", self.name)

    def bye(self):
        """" Bye """
        print("Bye,", self.name)

    def getName(self):
        """ Returns the name """
        return self.name    
    
# Import class from myClassExample.py
import myClassExample

# Create an object with a specific constructor
myObject = myClassExample.helperClass("My Name")

# Use the functions provides by the class
myObject.hi()
myObject.bye()

print("The name is", myObject.getName())



# What to try out
#################
# - Start running all available examples
# - Create the class "myClassExample.py" in this directory. Compare it
# with the output of this program.
# - Extend the example class: The name should be changeable using a method after
# the class got instantiated.
# - Solve the library project 
