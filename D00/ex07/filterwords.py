import sys

if len(sys.argv) != 3:
    print("ERROR")
    exit()
string = sys.argv[1]
try:
    string = int(string)
    print("ERROR2")
    exit()
except ValueError:
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("ERROR3")
        exit()


def filter(string, n):
    resul = []
    liste = string.split(" ")
    for i in range(len(liste)):
        if (len(liste[i]) > n):
            resul.append(liste[i])
    print(resul)


filter(string, n)
