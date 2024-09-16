class Animal:
    name = ""
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def display(self):
        print("My name is ", self.name)

    def eat(self):  # Method Overriding
        super().eat()
        print("I eat Bones")

labrador = Dog()
labrador.name = "Rocky"
labrador.eat()
labrador.display()

# Method Overriding & Super Keyword
jitu = Animal()
jitu.eat() # I can eat

jitu = Dog()
jitu.eat() # I can eat - I eat Bones





