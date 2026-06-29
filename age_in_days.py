# Program: Age in Days Calculator
# Description: Converts age in years to the number of days lived.
# Covers: Functions, loops, exception handling, user input.

def age_in_days():
    print("Calculate how many days you have lived.")
    while True:
        try:
            age = int(input("Enter your age in years: "))
            days = age * 365
            print(f"You have lived approximately {days} days.")
        except ValueError:
            print("Please enter a valid number.")
        choice = input("Calculate again? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye!")
            break

age_in_days()
