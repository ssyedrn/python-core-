# Program: Food Delivery System
# Description: Simulates a food ordering system where customers can add items and view totals.
# Covers: Classes, encapsulation, properties, instance methods,
#         and static methods.

class FoodItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    def info(self):
        return f"{self._name} - {self._price}"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item: FoodItem):
        self.items.append(item)
        return f"{item.info()} added to order."

    def total(self):
        return sum(i.price for i in self.items)

class Restaurant:
    @staticmethod
    def greet():
        return "Welcome to our restaurant."

i1 = FoodItem("Burger", 120)
i2 = FoodItem("Pizza", 250)
o = Order("abc")
print(o.add_item(i1))
print(o.add_item(i2))
print("Total:", o.total())
print(Restaurant.greet())
