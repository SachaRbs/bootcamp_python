import sys

string = ""
for arg in sys.argv:
    if (arg != sys.argv[0]):
        string = string + arg + " "

string = string.strip()
string = string.swapcase()

print(string[::-1])
