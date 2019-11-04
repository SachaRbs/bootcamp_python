import random


def game():
    cpt = 0
    number = random.randint(1, 99)
    inp = 0
    print("This is an interactive guessing game!\n" +
          "You have to enter a number between 1 and 99 " +
          "to find out the secret number.\n" +
          "Type 'exit' to end the game.\nGood luck!")
    while(inp != number):
        inp = input("What's your guess between 1 and 99?\n>>")
        try:
            inp = int(inp)
            cpt += 1
        except ValueError:
            if (inp == "exit"):
                print("Goodbye!")
                exit()
            else:
                print("Wrong enter a number between 1 and 99 or exit")
                continue
        if inp > number:
            print("Too high!")
        if inp < number:
            print("Too low!")
    if inp == 42:
        print("The answer to the ultimate question of life," +
              "the universe and everything is 42.")
    if cpt == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("Congratulations, you've got it!\n" +
              "You won in " + str(cpt) + " attempts!")


game()
