# Program: Contact Book
# Description: Add and view contacts stored in a JSON file.
# Covers: JSON file handling, functions, exception handling, user input.

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    try:
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load contacts: {e}")
        return {}

def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE, 'w') as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        print(f"Failed to save contacts: {e}")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    phone = input(f"Enter phone number for {name}: ").strip()
    if not phone.isdigit():
        print("Phone number should contain digits only.")
        return
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"  {name}: {phone}")

def main():
    contacts = load_contacts()
    while True:
        action = input("Add contact (a), View contacts (v), Quit (q): ").lower()
        if action == 'a':
            add_contact(contacts)
            save_contacts(contacts)
        elif action == 'v':
            view_contacts(contacts)
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a, v, or q.")

if __name__ == "__main__":
    main()
