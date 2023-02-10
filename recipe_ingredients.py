from sql_connection import SQLiteConnection
class Recipeingredients:

    def __init__(self):
        self.ingredient_sql = ()
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()

    # iterate over ingredient list and display them to user
    def list_ingredients(self, name):

        # fetch all ingredients for the selected recipe
        self.c.execute("SELECT * FROM recipes WHERE recipe=? AND type='ingredient'", (name,))
        items = self.c.fetchall()

        # if there were no ingredients print a message
        # if there is ingredients, print them and return the list
        if not items:
            print('No ingredients yet...')
        else:
            for item in range(len(items)):
                print(f'{item+1}: {items[item][5]}')
            return items

    # add new ingredient to list
    def input_ingredient(self, name, date_added):

        # ask user for new ingredient
        print('== Input details of new ingredient ==')
        new_ingredient = input('ingredient: ')

        # input the new ingredient data entry
        self.ingredient_sql = (name, date_added,'', 'ingredient','', new_ingredient)
        sql = ("INSERT INTO recipes VALUES (?, ?, ?, ?, ?, ?)")
        self.c.execute(sql, self.ingredient_sql)
        self.connect.commit()

    # change an ingredient that already exists
    def change_ingredient(self, choice, items, name, date_added):

        # turn user choice into list location and print the users ingredient choice
        choice = choice-1
        print(f'Current ingredient: {items[choice][5]}')
        print('====================')

        # ask user for new ingredient and update the data entry
        new_ingredient = input('New ingredient: ')
        sql = """UPDATE recipes SET recipe=?,
                'date added'=?,
                'last cooked'=?,
                type=?,
                step=?,
                details=?
                WHERE recipe=? AND details=? """
        new_ingredient = (name, date_added,'', 'ingredient','', new_ingredient, name, items[choice][5])
        self.c.execute(sql, new_ingredient)
        self.connect.commit()

    # delete an ingredient that already exists
    def delete_ingredient(self, choice, name, ingredient_list):
        choice = choice-1

        # delete the data entry in the database
        sql = ("DELETE FROM recipes WHERE recipe=? AND details=?")
        del_choice = (name, ingredient_list[choice][5])
        self.c.execute(sql, del_choice)
        self.connect.commit()