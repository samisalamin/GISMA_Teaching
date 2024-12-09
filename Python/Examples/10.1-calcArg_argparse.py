"""_summary_

    Returns:
        _type_: _description_
    Usage:
        calcArg.py <operation> <operand1> <operand2>
    Example:
        calcArg.py add 5 3 
"""

import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("operand1", type=float, help="First operand")
    parser.add_argument("operand2", type=float, help="Second operand")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.operand1, args.operand2)
    elif args.operation == "subtract":
        result = subtract(args.operand1, args.operand2)
    elif args.operation == "multiply":
        result = multiply(args.operand1, args.operand2)
    elif args.operation == "divide":
        result = divide(args.operand1, args.operand2)

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()