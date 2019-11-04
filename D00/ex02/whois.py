import sys

if len(sys.argv) > 2:
    print("ERROR")
elif len(sys.argv) > 1:
    try:
        value = int(sys.argv[1])
        if value == 0:
            print("I'm Zero.")
        elif value % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("ERROR")
