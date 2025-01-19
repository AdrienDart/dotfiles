import math
from random import choice


def squareRoot(number):
    return math.sqrt(number)


def randomChoice(items):
    return choice(items)


def main():
    print("Square root of 16 is:", squareRoot(16))
    print("Random choice from list:", randomChoice([1, 2, 3, 4, 5]))


main()
