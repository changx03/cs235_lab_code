import random
from numberChecker import *

def pickANumber(even, prime):
    number = random.randint(1, 100)
    if even:
        if not checkIsEven(number):
            pickANumber(even, prime)
    
    if prime:
        if not checkIsPrime(number):
            pickANumber(even, prime)

    return random.randint(1, 100)
