import random
from numberChecker import *

def pickANumber(even, prime):
    number = random.randint(1, 100);
    if even:
        if not checkIsEven(number):
            pickANumber()
    
    if prime:
        if not checkIsPrime(number):
            pickANumber()

    return random.randint(1, 100)
