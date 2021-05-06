import json
from json import JSONEncoder


class Employee:
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address


class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin


# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


address = Address("Alpharetta", "7258 Spring Street", "30004")
employee = Employee("John", 9000, address)


print("Printing to check how it will look like")
print(EmployeeEncoder().encode(employee))
