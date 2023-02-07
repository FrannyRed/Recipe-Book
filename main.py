import os
from recipe_ingrediants import RecipeIngrediants
from recipe_instructions import RecipeInstructions
from recipe_page import RecipePage

# initialize classes
ingrediants = RecipeIngrediants()
instructions = RecipeInstructions()
recipe_page = RecipePage()

# program loop
os.system('cls')
name = input('What is the name of your recipe?: ')

while True:
    os.system('cls')
    recipe_page.recipe_name(name)
    recipe_page.show_ingrediants(ingrediants)
    recipe_page.show_instructions(instructions)
    choice = recipe_page.user_choices()

    if choice == 1: # input new ingrediant
        os.system('cls')
        ingrediants.input_ingrediant()

    elif choice == 2:   # change an ingrediant
        selection = int(input('Choose ingrediant: '))
        os.system('cls')
        ingrediants.change_ingrediant(selection)

    elif choice == 3:   # delete an ingrediant
        selection = int(input('Choose ingrediant: '))
        ingrediants.delete_ingrediant(selection)

    elif choice == 4:   # add an instruction step
        os.system('cls')
        instructions.add_instructions()

    elif choice == 5:   # change an instruction step
        selection = int(input('Choose instruction step:'))
        os.system('cls')
        instructions.change_instructions()

    elif choice == 6:   # delete an instruction step
        selection = int(input('Choose instruction step:'))
        instructions.delete_instructions()

    elif choice == 7:   # return to the list of recipes (currently exits the program)
        os.system('cls')
        break