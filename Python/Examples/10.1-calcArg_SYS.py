"""_summary_

    Returns:
        _type_: _description_
    Usage:
        calcArg.py <operation> <operand1> <operand2>
    Example:
        calcArg.py add 5 3 
"""

import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <operand1> <operand2>")
        sys.exit(1)

    operation = sys.argv[1]
    operand1 = float(sys.argv[2])
    operand2 = float(sys.argv[3])

    if operation == "add":
        result = add(operand1, operand2)
    elif operation == "subtract":
        result = subtract(operand1, operand2)
    elif operation == "multiply":
        result = multiply(operand1, operand2)
    elif operation == "divide":
        result = divide(operand1, operand2)
    else:
        print("Unknown operation. Available operations: add, subtract, multiply, divide")
        sys.exit(1)

    print(f"The result is: {result}")