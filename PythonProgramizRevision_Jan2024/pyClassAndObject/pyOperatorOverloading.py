# Overloading + operator
class Point:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)  # p3 object is created by returning this


p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3.x, p3.y)


# Overloading comparison operator
class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def __lt__(self, other):
        if self.age < other.age:
            return True
        else:
            return False


p1 = Person("Bapu", 35);
p2 = Person("Bapi", 34);
print(p1 > p2)
print(p2 > p1)

"""
Advantages of Operator Overloading:
1. Improves code readability by allowing the use of familiar operators.
2. Ensures that objects of a class behave consistently with built-in types and other user-defined types.
Makes it simpler to write code, especially for complex data types.
Allows for code reuse by implementing one operator method and using it for other operators.
"""
