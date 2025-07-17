
#1- 
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

#2- 

# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")


#3- 
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

#4- 
x = [4, 6, 8, 24, 12, 2]
def maxs(x):
x.sort(reverse=True)
return x[0]
print(maxs(x))


#5- 
def count_upper_lower_chars(input_string):
    char_count = {"uppercase": 0, "lowercase": 0, "other": 0}
    for char in input_string:
        if char.isupper():
            char_count["uppercase"] += 1
        elif char.islower():
            char_count["lowercase"] += 1
        else:
            char_count["other"] += 1
    return char_count
 
sentence = "Hello, Python! How are you?"
result = count_upper_lower_chars(sentence)
 
print(result)
 
# output:
# {'uppercase': 3, 'lowercase': 17, 'other': 7}

#6-

def shortest_longest_words(words_list):
    shortest_word = min(words_list, key=len)
    longest_word = max(words_list, key=len)
    return shortest_word, longest_word
 
words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
result = shortest_longest_words(words)
 
print(result)
 
# output:
# ('kiwi', 'grapefruit')

#7-
def add_unique_element(input_list, element):
    if element not in input_list:
        input_list.append(element)
 
my_list = ["apple", "banana", "kiwi"]
add_unique_element(my_list, "banana")
add_unique_element(my_list, "orange")
 
print(my_list)
 
# output:
# ['apple', 'banana', 'kiwi', 'orange']