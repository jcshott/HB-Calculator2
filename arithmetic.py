def add(args):
    print args
    total = 0
    for element in args:
        total += int(element)
       # print total
    return total


def subtract(args):
    total = int(args[0])
    for element in args[1:]:
        total -= int(element)
    return total


def multiply(args):
    total = 1
    for element in args:
        total = total * int(element)
    return total


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return int(num1) * int(num1)


def cube(num1):
    # Needs only one argument
    return int(num1) * int(num1) * int(num1)


def power(num1, num2):
    return int(num1) ** int(num2)  # ** = exponent operator


def mod(num1, num2):
    return int(num1) % int(num2)
 