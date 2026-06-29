# Program: Mini Quiz
# Description: A multiple choice quiz with score tracking.
# Covers: Dictionaries, functions, loops, exception handling, user input.

questions = {
    "What is the capital of France?": "paris",
    "What is 2 + 2?": "4",
    "Who wrote 'To be, or not to be'?": "shakespeare",
    "What color do you get when you mix red and white?": "pink",
    "Which planet is known as the Red Planet?": "mars",
    "What is the boiling point of water in Celsius?": "100",
    "What language is primarily spoken in Brazil?": "portuguese",
    "Who painted the Mona Lisa?": "da vinci"
}

def play_quiz():
    score = 0
    print("Welcome to the quiz!")
    for q, a in questions.items():
        answer = input(q + " ").strip().lower()
        if answer == a:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The answer was '{a}'.")
    print(f"Quiz over. You scored {score} out of {len(questions)}.")

def main():
    while True:
        play_quiz()
        choice = input("\nPlay again? (y/n): ").strip().lower()
        if choice == 'n':
            print("Goodbye!")
            break
        elif choice == 'y':
            print("Starting again!")
        else:
            print("Invalid input. Exiting.")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
