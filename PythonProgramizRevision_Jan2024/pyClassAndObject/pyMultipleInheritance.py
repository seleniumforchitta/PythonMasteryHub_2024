# Python Multiple Inheritance

class A:
    def aInfo(self):
        print("I am in class A")


class B:
    def bInfo(self):
        print("I am in class B")


class C(A, B):
    pass


c = C()
c.aInfo()  # I am in class A
c.bInfo()  # I am in class B


# Python Multilevel Inheritance
class SuperClass:

    def super_method(self):
        print("Super Class method called")


# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")


# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"


# Method Resolution Order (MRO) in Python
class SuperClass1:
    def info(self):
        print("Super Class 1 method called")


class SuperClass2:
    def info(self):
        print("Super Class 2 method called")


class Derived(SuperClass1, SuperClass2):
    pass


d1 = Derived()
d1.info()  # Super Class 1 method called

# In this case, the MRO specifies that methods should be inherited from the leftmost superclass first, so info() of
# SuperClass1 is called rather than that of SuperClass2.
