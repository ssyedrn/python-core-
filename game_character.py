# Program: Game Character System
# Description: Represents game characters with different attack styles using polymorphism.
# Covers: Abstract classes, inheritance, polymorphism,
#         method overriding, and static methods.

from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @abstractmethod
    def attack(self):
        pass

    def info(self):
        return f"{self._name} | HP: {self._hp}"

class Warrior(Character):
    def attack(self):
        return f"{self._name} attacks with a sword."

class Mage(Character):
    def attack(self):
        return f"{self._name} casts a fireball."

class Arena:
    @staticmethod
    def welcome():
        return "Welcome to the arena."

w = Warrior("Brute", 120)
m = Mage("SparkleBoy", 80)
print(w.info(), w.attack())
print(m.info(), m.attack())
print(Arena.welcome())
