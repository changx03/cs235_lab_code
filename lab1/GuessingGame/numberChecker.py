def checkIsEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def checkIsPrime(number):
    #This function isn't sure how to check if a number is prime, so it simply excludes even numbers.
    for i in range(2,number):
        if (number%i) == 0:
            return False
    return True

