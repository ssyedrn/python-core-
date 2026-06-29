# Program: Notes App
# Description: A simple notes app to add and view notes stored in a text file.
# Covers: File handling, functions, exception handling, user input.

import os

NOTES_FILE = "notes.txt"

def add_note():
    note = input("Enter your note: ").strip()
    if not note:
        print("Note cannot be empty.")
        return
    try:
        with open(NOTES_FILE, 'a') as f:
            f.write(note + "\n")
        print("Note saved.")
    except Exception as e:
        print(f"Failed to save note: {e}")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    try:
        with open(NOTES_FILE, 'r') as f:
            notes = f.readlines()
        if not notes:
            print("No notes found.")
        else:
            print("Your notes:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
    except Exception as e:
        print(f"Error reading notes: {e}")

def main():
    while True:
        choice = input("Add note (a), View notes (v), Quit (q): ").lower()
        if choice == 'a':
            add_note()
        elif choice == 'v':
            view_notes()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a, v, or q.")

if __name__ == "__main__":
    main()
