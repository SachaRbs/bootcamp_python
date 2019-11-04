import sys


def operations(a, b):
    print("Sum: " + str(a + b))
    print("Difference: " + str(a - b))
    print("Product: " + str(a * b))
    if b != 0:
        print("Quotient: " + str(a / b))
        print("Remainder: " + str(a % b))
    else:
        print("Quotient: ERROR (div by zero")
        print("Remainder: ERROR (modulo by zero)")


if len(sys.argv) > 3:
    print("InputError: too many arguments")
if len(sys.argv) < 3:
    print("Usage: python operations.py\nExample:\npython operations.py 10 3")
else:  # check si nb == "4" et ppas 4
    operations(int(sys.argv[1]), int(sys.argv[2]))
