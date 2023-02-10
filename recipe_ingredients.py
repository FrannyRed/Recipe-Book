from sql_connection import SQLiteConnection
class Recipeingredients:

    def __init__(self):
        self.ingredient_sql = ()
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()

    # iterate over ingredient list and display them to user
    def list_ingredients(self, name):
        self.c.execute("SELECT * FROM recipes WHERE recipe=? AND type='ingredient'", (name,))
        items = self.c.fetchall()
        if not items:
            print('No ingredients yet...')
        else:
            for item in items:
                print(item)
            return items

    # add new ingredient to list
    def input_ingredient(self, name):
        print('== Input details of new ingredient ==')
        new_ingredient = input('ingredient: ')
        self.c.execute("SELECT * FROM recipes WHERE recipe=? AND type='placeholder'", (name,))
        date_added = self.c.fetchone()
        date_added = date_added[1]
        self.ingredient_sql = (name, date_added,'', 'ingredient','', new_ingredient)
        sql = ("INSERT INTO recipes VALUES (?, ?, ?, ?, ?, ?)")
        self.c.execute(sql, self.ingredient_sql)
        self.connect.commit()

    # change an ingredient that already exists
    def change_ingredient(self, choice, items):
        choice = choice-1
        print(f'Current ingredient: {items[choice]}')
        print('====================')
        new_ingredient = input('New ingredient: ')
        sql = """UPDATE recipes SET recipe=?,
                'date added'=?,
                'last cooked'=?,
                type=?,
                step=?,
                details=?
                WHERE recipe=? AND details=? """
        

    # delete an ingredient that already exists
    def delete_ingredient(self, choice):
        choice = choice-1
        del self.ingredient_row[choice]