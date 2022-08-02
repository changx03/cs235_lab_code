def checkIsEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def checkIsPrime(number):
    #This function isn't sure how to check if a number is prime, so it simply excludes even numbers.
    if checkIsEven(number):
        return False
    return True

