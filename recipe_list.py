from sql_connection import SQLiteConnection
from recipe_page import RecipePage
from datetime import datetime
import os

# TODO make data validation for new recipes so there is no duplicating recipe names

class RecipeList:

    def __init__(self):
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()

    def list_recipes(self):
        self.c.execute("SELECT DISTINCT recipe FROM recipes")
        items = self.c.fetchall()
        if not items:
            print('No recipes yet...')
        else:
            for item in range(len(items)):
                print(f'{item+1}: {items[item][0]}')
            return items

    def new_recipe(self, page):
        name = input('What is the name of your new recipe?: ')
        today = datetime.today().strftime('%m-%d-%Y')
        sql = ("INSERT INTO recipes VALUES (?, ?, ?, ?, ?, ?)")
        recipe_input = (name, today, '', 'placeholder', '', 'placeholder')
        self.c.execute(sql, recipe_input)
        self.connect.commit()
        page.recipe_page_program_loop(name)

    def choose_recipe(self, list, page):
        selection = int(input('Choose recipe to open: '))
        name = list[selection-1][0]
        page.recipe_page_program_loop(name)

    def remove_recipe(self, list):
        selection = int(input('Choose recipe to delete: '))
        name = list[selection-1][0]
        self.c.execute("DELETE FROM recipes WHERE recipe=?", (name,))
        self.connect.commit()

    def user_choices(self):
        choice = int(input("""
*** Program Options ***

New Recipe: 1
Choose Recipe: 2
Delete Recipe: 3
Exit Program: 4

Input Here: """))
        return choice

    # recipe list program loop
    def recipe_list_program_loop(self):
        while True:
            os.system('cls')
            screen = RecipeList()
            page = RecipePage()
            list = screen.list_recipes()
            choice = self.user_choices()

            if choice == 1: # make a new recipe
                screen.new_recipe(page)

            elif choice == 2:   # choose an existing recipe to open
                screen.choose_recipe(list, page)

            elif choice == 3:   # delete a recipe
                screen.remove_recipe(list)

            elif choice == 4:   # exit the program
                break