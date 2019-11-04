t = (19, 42, 21)
string = "The " + str(len(t)) + " numbers are: "
for i in range(len(t)):
    string = string + str(t[i])
    if i < len(t) - 1:
        string = string + ", "

print(string)
