def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print("Addition of 19 and 97 is:", add(19, 97))
    print("Subtraction of 12 from 27 is:", subtract(12, 27))
    print("Multiplication of 11 and 8 is:", multiply(11, 8))
    print("Division of 12954 by 3 is:", divide(12954, 3))
