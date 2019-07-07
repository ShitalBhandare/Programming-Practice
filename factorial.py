import os
import math

def factorial(no):
    if no == 0:
        return 1
    else:
        return no * factorial(no - 1)

if __name__ == '__main__':
    no = input("Enter any number:")
    fact = factorial(no)
    print("Factorial of " + str(no) + " = " + str(fact))




