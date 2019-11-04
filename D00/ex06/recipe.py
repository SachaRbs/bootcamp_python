import sys

cookbook = {
    "sandwich": {
                "ingredients": ["ham", "bread", "cheese", "tomatoes"],
                "meal": "lunch",
                "prep_time": 10
                },
    "cake":     {
                "ingredients": ["flour", "sugar", "eggs"],
                "meal": "dessert",
                "prep_time": 60
                },
    "salade":    {
                "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
                "meal": "lunch",
                "prep_time": 15
                }
}


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients
    cookbook[name]['meal'] = meal
    cookbook[name]['prep_time'] = prep_time


def print_recipe(name):
    if name in cookbook:
        print("Recipe for " + name + ":")
        print("Ingredients list: " + str(cookbook[name]["ingredients"]))
        print("To be eaten for " + str(cookbook[name]["meal"]) + ".")
        print("Takes " + str(cookbook[name]["prep_time"])
              + " minutes of cooking.")


def delete_recipe(name):
    if name in cookbook:
        del cookbook[name]


def print_name():
    print("Recipe available :")
    i = 1
    for key in cookbook:
        print(str(i) + " : " + str(key))
        i += 1


def menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe\n2: Delete a recipe\n" +
          "3: Print a recipe\n4: Print the cookbook\n5: Quit")
    try:
        a = int(input(">> "))
        if a == 1:
            name = input("Please enter the recipe's name\n")
            ingredients = input("Please enter the recipe's ingredients," +
                                "only separate by ';'\n")
            meal = input("Please enter the recipe's meal type\n")
            prep_time = input("Please enter the recipe's preparation time\n")
            ingredients = ingredients.split(";")
            add_recipe(name, ingredients, meal, prep_time)
        if a == 2:
            name = input("Please enter the recipe's name " +
                         "that you want to delete\n")
            delete_recipe(name)
        if a == 3:
            name = input("Please enter the recipe's name " +
                         "that you want to print\n")
            print_recipe(name)
        if a == 4:
            print_name()
        if a == 5:
            return(0)
    except ValueError:
        print("This option does not exist, please type the " +
              "corresponding number.\nTo exit, enter 5.")
    return(1)


loop = 1
while(loop):
    loop = menu()
