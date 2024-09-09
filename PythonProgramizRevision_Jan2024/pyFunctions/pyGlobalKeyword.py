c = 1
def globaltest():
    global c
    c = c + 2
    print(c)


globaltest()  # UnboundLocalError: cannot access local variable 'c' where it is not associated with a value
