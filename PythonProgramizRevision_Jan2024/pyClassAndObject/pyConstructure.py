# We can initialize the values of data members using constructures
class Bikes:
    def __init__(self, name=""):
        self.name = name


bike1 = Bikes()
print(bike1.name)  # Blank
bike2 = Bikes("Apache")
print(bike2.name)  # Apache
