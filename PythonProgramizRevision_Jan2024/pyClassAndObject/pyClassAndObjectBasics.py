# An object is simply a collection of data (variables) and methods (functions).
# Similarly, a class is a blueprint for that object.

# class ClassName:
#       # Definition

class Bike:
    name = ""
    gear = 0


bike1 = Bike()  # This is how object is created
bike1.name = "Apache"
bike1.gear = 5

print(f"Bike Name: {bike1.name} and it has {bike1.gear} gears")
