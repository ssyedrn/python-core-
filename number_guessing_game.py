# Program: Number Guessing Game
# Description: Guess a randomly generated number between 1 and 20.
# Covers: Random module, loops, exception handling, user input.

import random

def guessing_game():
    print("Guess the number between 1 and 20.")
    while True:
        number = random.randint(1, 20)
        attempts = 0
        while True:
            try:
                guess = int(input("Your guess: "))
                attempts += 1
                if guess < number:
                    print("Too low. Try higher.")
                elif guess > number:
                    print("Too high. Try lower.")
                else:
                    print(f"Correct! You got it in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")
        choice = input("Play again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

guessing_game()
