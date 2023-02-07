import os
from recipe_ingrediants import RecipeIngrediants
from recipe_instructions import RecipeInstructions

# TODO add ingredients to a SQL database

class RecipePage:
    
    def recipe_name(self, name):
        print(f'===============  {name}  ===============')

    # show user the current list of ingrediants
    def show_ingrediants(self, ingrediants):
        print('\n##########   Ingrediants   ##########\n')
        ingrediants.list_ingrediants()
        print()

    # show recipe instructions to user
    def show_instructions(self, instructions):
        print('\n##########   Instructions    ##########\n')
        instructions.list_instructions()

    # give user their list of choices
    def user_choices(self):
        choice = int(input('''
+++ Program Options +++
Add Ingrediant: 1
Change Ingrediant: 2
Delete Ingrediant: 3
Add Instruction Step: 4
Change Instruction Step: 5
Delete Instruction Step: 6
Back To Recipe List: 7
Input Here: '''))
        print()
        return choice


# initialize classes
ingrediants = RecipeIngrediants()
instructions = RecipeInstructions()
page = RecipePage()

# test program
os.system('cls')
name = input('What is the name of your recipe?: ')

while True:
    os.system('cls')
    page.recipe_name(name)
    page.show_ingrediants(ingrediants)
    page.show_instructions(instructions)
    choice = page.user_choices()

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