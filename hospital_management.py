# Program: Hospital Management System
# Description: Models patients and doctors in a hospital with appointment scheduling.
# Covers: Abstract classes, encapsulation, properties, inheritance,
#         __str__, static methods, and class methods.

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self._name} | Age: {self._age} | Role: {self.role()}"

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def role(self):
        return "Doctor"

    def consult(self, patient):
        return f"Dr. {self._name} is consulting {patient.name}."

class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self._ailment = ailment

    def role(self):
        return "Patient"

    @property
    def ailment(self):
        return self._ailment

class Hospital:
    hospital_name = "City Hospital"

    def __init__(self):
        self.appointments = []

    def book_appointment(self, doctor: Doctor, patient: Patient):
        self.appointments.append((doctor, patient))
        return f"Appointment booked: {doctor.name} with {patient.name}."

    def __len__(self):
        return len(self.appointments)

    @classmethod
    def update_name(cls, name):
        cls.hospital_name = name
        return f"Hospital renamed to {name}."

    @staticmethod
    def helpline():
        return "Helpline: 1800-000-000"

d = Doctor("Smith", 45, "Cardiology")
p = Patient("John", 30, "Fever")
h = Hospital()
print(d)
print(p)
print(h.book_appointment(d, p))
print("Total appointments:", len(h))
print(Hospital.update_name("Metro Hospital"))
print(Hospital.helpline())
