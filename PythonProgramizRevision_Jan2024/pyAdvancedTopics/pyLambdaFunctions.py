# Lambda Function
# def double(n):
#       return n*2
double = lambda n: n * 2
print(double(10))

greet = lambda: print("Hello")
greet()

greet = lambda name="Default": print("Hello", name)
greet("Bapu")



