# TODO add ingredients to a SQL database

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