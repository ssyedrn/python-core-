# Program: Employee Payroll System
# Description: Manages employee records and calculates bonuses based on employment type.
# Covers: Inheritance, encapsulation, properties, method overriding,
#         and static methods.

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value

    def info(self):
        return f"{self._name} earns {self._salary}"

class FullTime(Employee):
    def calculate_bonus(self):
        return self._salary * 0.1

class PartTime(Employee):
    def calculate_bonus(self):
        return self._salary * 0.03

class HR:
    @staticmethod
    def announce():
        return "Payroll processing is underway."

e1 = FullTime("abc", 50000)
e2 = PartTime("xyz", 20000)
print(e1.info(), "Bonus:", e1.calculate_bonus())
print(e2.info(), "Bonus:", e2.calculate_bonus())
print(HR.announce())
