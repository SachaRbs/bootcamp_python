import sys

alphabet = {
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-.. ",
    "e": ". ",
    "f": "..-. ",
    "g": "--. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    " ": "/ "
}


def morse_code(string):
    morse = ""
    for c in string:
        if c in alphabet:
            morse = morse + alphabet[c]
        else:
            print("ERROR")
            exit()
    print(morse)


if len(sys.argv) > 1:
    string = ""
    for arg in sys.argv:
        if (arg != sys.argv[0]):
            string = string + arg + " "
    morse_code(string.lower().strip())
