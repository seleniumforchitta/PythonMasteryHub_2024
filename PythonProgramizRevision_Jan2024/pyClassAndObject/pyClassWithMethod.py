# A python function defined inside a class is called method
class Calculation:
    x = 0
    y = 0

    def calculate(self, x, y, symbol): # self is passed as an argument in methods
        if symbol == '+':
            return x + y
        elif symbol == '-':
            return x - y
        elif symbol == '*':
            return x * y
        elif symbol == '/':
            return x / y


add = Calculation()
add.x = 5
add.y = 2
value = add.calculate(add.x, add.y, "*")
print(value)
