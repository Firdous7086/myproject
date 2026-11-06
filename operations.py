
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def percentage(a, b):
    return (a / 100) * b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number!"
    return a ** 0.5
