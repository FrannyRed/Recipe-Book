class RecipeIngrediants:

    def __init__(self):
        self.ingrediant_row = []

    # iterate over ingrediant list and display them to user
    def list_ingrediants(self):
        for row in range(len(self.ingrediant_row)):
            print(f'{row+1}: {self.ingrediant_row[row]}')

    # add new ingrediant to list
    def input_ingrediant(self):
        print('== Input details of new ingrediant ==')
        # TODO add data validation
        new_ingrediant = input('Ingrediant: ')
        self.ingrediant_row.append(new_ingrediant)

    # change an ingrediant that already exists
    def change_ingrediant(self, choice):
        choice = choice-1
        print('Current ingrediant:')
        print(f'{self.ingrediant_row[choice]}')
        print('== Input details of new ingrediant ==')
        new_ingrediant = input('Ingrediant: ')
        self.ingrediant_row[choice] = new_ingrediant

    def delete_ingrediant(self, choice):
        choice = choice-1
        del self.ingrediant_row[choice]