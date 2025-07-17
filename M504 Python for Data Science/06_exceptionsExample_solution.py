# Define a function named get_numeric_input that takes a prompt as a parameter.
def get_numeric_input(prompt):
    # Use a while loop to repeatedly prompt the user until a valid numeric input is provided.
    while True:
        try:
            # Attempt to get a numeric input (float) from the user and store it in the 'value' variable.
            value = float(input(prompt))
            # Return the numeric value.
            return value
        except ValueError:
            # Handle the exception if the user's input is not a valid number.
            print("Error: Invalid input. Please Input a valid number.")

# Usage
# Call the get_numeric_input function to get the first numeric input from the user with the provided prompt.
n1 = get_numeric_input("Input the first number: ")
# Call the get_numeric_input function to get the second numeric input from the user with the provided prompt.
n2 = get_numeric_input("Input the second number: ")
# Calculate the product of the two input numbers.
result = n1 * n2
# Print the result, which is the product of the two numbers.
print("Product of the said two numbers:", result)


#######################################################

# Define a function named test_index that takes 'data' and 'index' as parameters.
def test_index(data, index):
    try:
        # Try to access an element at the specified 'index' in the 'data' list and store it in the 'result' variable.
        result = data[index]
        # Perform desired operation using the result (in this case, printing it).
        print("Result:", result)
    except IndexError:
        # Handle the exception if the specified 'index' is out of range for the 'data' list.
        print("Error: Index out of range.")

# Define a list of numbers 'nums'.
nums = [1, 2, 3, 4, 5, 6, 7]
# Prompt the user to input an index and store it in the 'index' variable.
index = int(input("Input the index: "))
# Call the test_index function with the 'nums' list and the user-provided 'index'.
test_index(nums, index)


###########################################################

# Try to execute the following block of code, which may raise exceptions.

# Prompt the user to input a number and attempt to convert it to an integer, storing it in the 'n' variable.
while True:
    try:
        n = int(input("Input a number: "))
        # If the user input is successfully converted to an integer, print the entered number.
        print("You entered:", n)
    # Handle the KeyboardInterrupt exception, which occurs when the user cancels the input (typically by pressing Ctrl+C).
    except KeyboardInterrupt:
        print("Input canceled by the user.")
        # Exit the loop if the user cancels the input.
        break


#########
# stopwatch in python
import time

def stopwatch():
    input("Press Enter to start the stopwatch")
    start_time = time.time()
    input("Press Enter to stop the stopwatch")
    end_time = time.time()
    
    elapsed_time = (end_time - start_time) * 1000000  # Convert seconds to microseconds
    print(f"Elapsed time: {elapsed_time:.0f} microseconds")

# Run the stopwatch function
stopwatch()

# a better implementation by disply the ongoing count of the stopwatch

import time

def stopwatch():
    input("Press Enter to start the stopwatch")
    start_time = time.time()
    
    try:
        while True:
            elapsed_time = (time.time() - start_time) * 1000000  # Convert seconds to microseconds
            print(f"Elapsed time: {elapsed_time:.0f} microseconds", end='\r')
            time.sleep(0.0001)  # Sleep for a short duration to reduce CPU usage
    except KeyboardInterrupt:
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000000  # Convert seconds to microseconds
        print(f"\nFinal elapsed time: {elapsed_time:.0f} microseconds")

# Run the stopwatch function
stopwatch()

