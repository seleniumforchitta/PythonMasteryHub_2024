def function_name():
    print("Hello")

function_name()
def greet(name):
    print("Hello", name);
greet("Jake");


def sumOfAllListMembers(list):
    sum = 0;
    for i in list:
        sum = sum + i;
    return sum;

def squaredNumFromList(list):
    list1 = [];
    for i in list:
        list1.append(i*i);
    return list1;

abc = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print(sumOfAllListMembers(abc));
print(squaredNumFromList(abc))

# Lambda Function
# def double(n):
#       return n*2
double = lambda n:n*2    # Lambda function doesn't have any name so they are also called anonymous function.
print(double(10))


