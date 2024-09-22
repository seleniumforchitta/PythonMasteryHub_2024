# Polymorphism in Addition operator
num1 = 12
num2 = 13
print(num1 + num2)

str1 = "Bapu"
str2 = "Bhai"
print(str1 + str2)

# Function Polymorphism
# Polymorphism of len() function
print(len("Automation"))
print(len({"Bapu", "Bhai", "Bhala", "Ki ?"}))
print(len(["Hmm", "Bhai", "Bhala"]))


# Class Polymorphism in Python
# Method Overloading
class Work:
    def work(self, name=None):
        if name is not None:
            print(name, " is working")
        else:
            print("I am working");


p1 = Work()
p1.work()
p1.work("Bapu")
p2 = Work()
p2.work("Ramesh")
""" Methods in Python can be called with zero, one, or more parameters. This process of calling the same method in
 different ways is called method overloading. Two methods cannot have the same name in Python; hence method overloading 
 is a feature that allows the same operator to have different meanings. """

# Method Overriding
"""When we define a method in child class that is already there in parent and provide a different application to it, 
then that is calling as method overriding"""


class Animal:
    def info(self):
        print("I am a Animal")


class Dog(Animal):
    def info(self):
        print("I am a Dog")
    pass


rocky = Dog()
doggy = Animal()
rocky.info() # Here it calls the overridden method of Child class. You can comment the child class method & test
doggy.info()
