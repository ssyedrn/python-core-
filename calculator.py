# Program: Calculator
# Description: A basic calculator that supports addition, subtraction, multiplication, and division.
# Covers: Functions, loops, exception handling, user input.

def calculator():
    print("Welcome to the calculator.")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            if op == '+':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif op == '-':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif op == '*':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif op == '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Invalid operation. Please use +, -, *, /.")
        except ValueError:
            print("Please enter valid numbers.")
        choice = input("Do another calculation? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye!")
            break

calculator()
