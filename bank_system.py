# Program: Bank System
# Description: Simulates a basic banking system using OOP concepts.
# Covers: Abstract classes, encapsulation, properties, inheritance,
#         static methods, class methods, and method overriding.

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, owner, balance=0):
        self.__acc_no = acc_no
        self.owner = owner
        self.__balance = balance

    @property
    def acc_no(self):
        return self.__acc_no

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        self.__balance += amount
        return f"{amount} deposited. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance."
        self.__balance -= amount
        return f"Withdrawn {amount}. Remaining: {self.__balance}"

class Savings(Account):
    def account_type(self):
        return "Savings"

class Current(Account):
    def account_type(self):
        return "Current"

class Customer:
    bank_name = "MyBank Ltd."

    def __init__(self, name, acc_no, acc_type="savings"):
        self.name = name
        if acc_type == "savings":
            self.account = Savings(acc_no, name)
        else:
            self.account = Current(acc_no, name)

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def update_bank(cls, new_name):
        cls.bank_name = new_name
        return f"Bank renamed to {new_name}"

    def info(self):
        return f"{self.name} | {self.account.acc_no} | {self.account.account_type()}"

c = Customer("xyz", 101)
print(c.info())
print(c.account.deposit(500))
print(c.account.withdraw(900))
print(c.account.withdraw(100))
print(Customer.update_bank("NewBank"))
