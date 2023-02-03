from recipe_ingrediants import RecipeIngrediants

# TODO add ingredients to a SQL database

class RecipePage:

    def __init__(self):
        pass

    def show_ingrediants(self, ingrediants):
        print('\n##########   Ingrediants   ##########\n')
        ingrediants.list_ingrediants()
        print()

    def user_choices(self):
        choice = int(input('Add Ingrediant: 1 = Change Ingrediant: 2 = Delete Ingrediant: 3 = Back To Recipe List: 4\nInput Here: '))
        print()
        return choice

    
ingrediants = RecipeIngrediants()
page = RecipePage()

while True:
    page.show_ingrediants(ingrediants)
    choice = page.user_choices()
    if choice == 1:
        ingrediants.input_ingrediant()
    elif choice == 4:
        break
    else:
        print('Please try again.')