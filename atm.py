# Program: Simple ATM
# Description: A basic ATM simulation with deposit, withdraw, and balance check.
# Covers: Classes, exception handling, loops, user input.

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def main():
    atm = ATM()
    while True:
        print("\nOptions: Deposit (d), Withdraw (w), Balance (b), Quit (q)")
        choice = input("Choose: ").lower()
        if choice == 'd':
            try:
                amt = float(input("Enter amount to deposit: "))
                atm.deposit(amt)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 'w':
            try:
                amt = float(input("Enter amount to withdraw: "))
                atm.withdraw(amt)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 'b':
            atm.check_balance()
        elif choice == 'q':
            print("Session ended. Goodbye!")
            break
        else:
            print("Invalid option. Please choose d, w, b, or q.")

if __name__ == "__main__":
    main()
