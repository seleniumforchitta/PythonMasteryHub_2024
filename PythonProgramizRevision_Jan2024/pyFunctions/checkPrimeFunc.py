# Write a function to check if a given number is prime or not.
def checkprime(num):
    if num <= 1:
        print(num, " is a prime number !")
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                print(num, " is not a prime number !")
                return
            else:
                print(num, " is a prime number !")
                return


checkprime(13)
checkprime(4)
checkprime(2)
checkprime(21)
checkprime(101)
checkprime(111)
checkprime(122)
checkprime(123)