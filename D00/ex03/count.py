import string


def text_analyzer(texte=""):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if texte == "":
        texte = input("What is the text to analyse?\n")
    upper = 0
    lower = 0
    punct = 0
    spaces = 0
    for c in texte:
        if c.islower():
            lower += 1
        if c.isupper():
            upper += 1
        if c == " ":
            spaces += 1
        if c in string.punctuation:
            punct += 1
    print("- " + str(upper) + " upper letters")
    print("- " + str(lower) + " lower letters")
    print("- " + str(punct) + " punctuation marks")
    print("- " + str(spaces) + "  spaces")


print(text_analyzer.__doc__)
