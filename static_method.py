#!/usr/bin/python3

# This is an example of the use of static methods
# Static methods are bound to the class
# This is a way to group functions

class calculator:

    @staticmethod
    def add(x, y):

        return x + y

    @staticmethod
    def subtract(x, y):

        return x - y

    @staticmethod
    def multiply(x, y):

        return x * y

    @staticmethod
    def divide(x, y):

        return x / y


def main():

    # Without instantiation

    calculator.add(1, 2)
    print(calculator.add(1, 2))
    print(calculator.subtract(2, 1))
    print(calculator.multiply(2, 3))
    print(calculator.divide(12, 3))

if __name__ == "__main__":

    main()
