# Local & Global
global_message = "Hi"


def greet():
    message = "Hello"  # Local Variable
    print(message)
    print(global_message)  # Hi


greet()
# print(message) # NameError: name 'message' is not defined
print(global_message)  # Hi


# Nonlocal
def first():
    msg = "Hello"
    print(msg)  # Hi

    def second():
        nonlocal msg
        msg = "2nd Hello"
        print(msg)  # 2nd Hello

    second()
    print(msg)  # 2nd Hello


first()
# Here the inner function could be able to change the value of msg by using nonlocal keyowrd

