from sql_connection import SQLiteConnection
class RecipeIngrediants:

    def __init__(self):
        self.ingrediant_row = []
        self.ingrediant_sql = ()
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()

    # iterate over ingrediant list and display them to user
    def list_ingrediants(self, name):
        for row in range(len(self.ingrediant_row)):
            print(f'{row+1}: {self.ingrediant_row[row]}')
        self.c.execute("SELECT * FROM recipes WHERE Recipe=? AND Type='ingrediant", (name,))
        items = self.c.fetchall()
        for item in items:
            print(item[3])

    # add new ingrediant to list
    def input_ingrediant(self, recipe_name):
        print('== Input details of new ingrediant ==')
        new_ingrediant = input('Ingrediant: ')
        self.ingrediant_sql = (recipe_name, 'ingrediant', "", new_ingrediant)
        self.c.execute("INSERT INTO recipes VALUES (?, ?, ?, ?)", self.ingrediant_sql)
        self.connect.commit()
        self.ingrediant_row.append(new_ingrediant)

    # change an ingrediant that already exists
    def change_ingrediant(self, choice):
        choice = choice-1
        print('Current ingrediant:')
        print(f'{self.ingrediant_row[choice]}')
        print('== Input details of new ingrediant ==')
        new_ingrediant = input('Ingrediant: ')
        self.ingrediant_row[choice] = new_ingrediant

    # delete an ingrediant that already exists
    def delete_ingrediant(self, choice):
        choice = choice-1
        del self.ingrediant_row[choice]