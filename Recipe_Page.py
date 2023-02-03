import os
from recipe_ingrediants import RecipeIngrediants

# TODO add ingredients to a SQL database

class RecipePage:

    def __init__(self):
        pass
    
    # show user the current list of ingrediants
    def show_ingrediants(self, ingrediants):
        print('\n##########   Ingrediants   ##########\n')
        ingrediants.list_ingrediants()
        print()

    # show recipe instructions to user
    def show_instructions(self, instructions):
        pass

    # give user their list of choices
    def user_choices(self):
        choice = int(input('Add Ingrediant: 1 / Change Ingrediant: 2 / Delete Ingrediant: 3 / Back To Recipe List: 4\nInput Here: '))
        print()
        return choice


# initialize classes
ingrediants = RecipeIngrediants()
page = RecipePage()

# test program
while True:
    os.system('cls')
    page.show_ingrediants(ingrediants)
    choice = page.user_choices()

    if choice == 1: # input new ingrediant
        os.system('cls')
        ingrediants.input_ingrediant()

    elif choice == 2:   # change an ingrediant
        selection = int(input('Choose ingrediant: '))
        os.system('cls')
        ingrediants.change_ingrediant(selection)

    elif choice == 4:   # return to the list of recipes (currently exits the program)
        os.system('cls')
        break