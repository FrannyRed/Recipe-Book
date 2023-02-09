import os
from recipe_ingrediants import RecipeIngrediants
from recipe_instructions import RecipeInstructions

# TODO add ingredients and instructions to a SQL database

class RecipePage:
    
    # print the recipe name
    def recipe_name(self, name):
        print(f'===============  Recipe: {name}  ===============')

    # show user the current list of ingrediants
    def show_ingrediants(self, ingrediants):
        print('\n############   Ingrediants   ############\n')
        ingrediants.list_ingrediants()
        print('\n#########################################')

    # show recipe instructions to user
    def show_instructions(self, instructions):
        print('\n-----------   Instructions    -----------\n')
        instructions.list_instructions()
        print('\n-----------------------------------------')

    # give user their list of choices
    def user_choices(self):
        choice = int(input('''
*** Program Options ***

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

    # the recipe page program loop
    def recipe_page_program_loop(self):

        # initialize classes
        ingrediants = RecipeIngrediants()
        instructions = RecipeInstructions()
        recipe_page = RecipePage()

        # get the name of the new recipe from the user
        os.system('cls')
        name = input('What is the name of your recipe?: ')

        # run the program loop
        while True:
            os.system('cls')
            recipe_page.recipe_name(name)
            recipe_page.show_ingrediants(ingrediants)
            recipe_page.show_instructions(instructions)
            choice = recipe_page.user_choices()

            if choice == 1: # input new ingrediant
                os.system('cls')
                ingrediants.input_ingrediant(name)

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