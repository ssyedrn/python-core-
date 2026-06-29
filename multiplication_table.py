# Program: Multiplication Table Generator
# Description: Generates a multiplication table for a given number.
# Covers: Functions, loops, exception handling, user input.

def generate_table():
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

try:
    generate_table()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
