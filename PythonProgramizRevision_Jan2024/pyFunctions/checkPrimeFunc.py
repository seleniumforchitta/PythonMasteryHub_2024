# Write a function to check if a given number is prime or not.
def checkprime(num):
    if num <= 1:
        print(num, " is not a prime number !")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(num, " is not a prime number !")
                return
            else:
                print(num, " is a prime number !")
                return


checkprime(0)
checkprime(1)
checkprime(13)
checkprime(4)
checkprime(2)
checkprime(21)
checkprime(101)
checkprime(122)
checkprime(123)

# o/p -
# 0  is not a prime number !
# 1  is not a prime number !
# 13  is a prime number !
# 4  is not a prime number !
# 21  is a prime number !
# 101  is a prime number !
# 111  is a prime number !
# 122  is not a prime number !
# 123  is a prime number !