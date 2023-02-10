import os
from recipe_ingredients import Recipeingredients
from recipe_instructions import RecipeInstructions
from sql_connection import SQLiteConnection

# TODO input status message for each user choice

class RecipePage:

    def __init__(self):
        self.ingredient_sql = ()
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()
    
    # print the recipe name
    def recipe_name(self, name):
        print(f'===============  Recipe: {name}  ===============')

    # show user the current list of ingredients
    def show_ingredients(self, ingredients, name):
        print('\n############   Ingredients   ############\n')
        ingredients_list = ingredients.list_ingredients(name)
        print('\n#########################################')
        return ingredients_list # return ingredients list to be used in other functions

    # show recipe instructions to user
    # TODO update instructions with SQL code
    def show_instructions(self, instructions):
        print('\n-----------   Instructions    -----------\n')
        instructions.list_instructions()
        print('\n-----------------------------------------')

    # give user their list of choices
    def user_choices(self):
        choice = int(input('''
*** Program Options ***

Add ingredient: 1
Change ingredient: 2
Delete ingredient: 3

Add Instruction Step: 4
Change Instruction Step: 5
Delete Instruction Step: 6

Back To Recipe List: 7

Input Here: '''))
        print()
        return choice

    # the recipe page program loop
    def recipe_page_program_loop(self, name):

        # initialize classes
        ingredients = Recipeingredients()
        instructions = RecipeInstructions()
        recipe_page = RecipePage()

        # find the create date for the recipe to add to the data entry
        self.c.execute("SELECT * FROM recipes WHERE recipe=? AND type='placeholder'", (name,))
        date_added = self.c.fetchone()
        date_added = date_added[1]

        # run the program loop
        while True:
            os.system('cls')
            recipe_page.recipe_name(name)
            ingredients_list = recipe_page.show_ingredients(ingredients, name)  # print the list of ingredients
            instructions_list = recipe_page.show_instructions(instructions) # print the list of instructions
            choice = recipe_page.user_choices() # run the user choice class method

            if choice == 1: # input new ingredient
                os.system('cls')
                ingredients.input_ingredient(name, date_added)

            elif choice == 2:   # change an ingredient
                try:
                    selection = int(input('Choose ingredient: '))
                    os.system('cls')
                    ingredients.change_ingredient(selection, ingredients_list, name, date_added)
                except:
                    pass

            elif choice == 3:   # delete an ingredient
                selection = int(input('Choose ingredient: '))
                ingredients.delete_ingredient(selection, name, ingredients_list)

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