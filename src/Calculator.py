import math


def addition(a, b):
    return float(a) + float(b)


# def subtraction(a, b):
#     return a - b

def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c


def multiplication(a, b):
    return float(b) * float(a)


def division(a, b):
    c = float(b) / float(a)
    return round(c, 9)


def squaring(a):
    return float(a) ** 2


def squarerooting(a):
    a = float(a)
    b = a ** 0.5
    return round(float(b), 8)


class Calculator:
    result = 0

    def __int__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def squareroot(self, a):
        self.result = squarerooting(a)
        return self.result
