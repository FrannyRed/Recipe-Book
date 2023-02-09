from sql_connection import SQLiteConnection

class RecipeList:

    def __init__(self):
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()

    # TODO use DISTINCT to make a list of all recipes listed in the database
    # TODO make a remove function that will delete a recipe by deleting all its rows in the database

    def list_recipes(self):
        self.c.execute("SELECT DISTINCT Recipe FROM recipes")
        items = self.c.fetchall()
        for item in items:
            print(item[0])
        return items

    def remove_recipe(self, name):
        self.c.execute("DELETE FROM recipes WHERE recipe=?", (name,))

    def user_choices(self):
        choice = int(input("""
*** Program Options ***

New Recipe: 1
Choose Recipe: 2
Delete Recipe: 3
Exit Program: 4

Input Here: """))

    def recipe_list_program_loop(self):
        page = RecipeList()
        list = page.list_recipes()
