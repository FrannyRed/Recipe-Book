class RecipeIngrediants:

    def __init__(self):
        self.ingrediant_row = []

    def list_ingrediants(self):
        for row in range(len(self.ingrediant_row)):
            print(f'{row+1}: {self.ingrediant_row[row][0]} - {self.ingrediant_row[row][1]} {self.ingrediant_row[row][2]}')

    def input_ingrediant(self):
        print('== Input details of new ingrediant ==')
        # TODO add data validation
        new_ingrediant = input('Ingrediant: ')
        new_value = input('Value: ')
        new_size = input('Size: ')
        ingrediant = [new_ingrediant, new_value, new_size]
        self.ingrediant_row.append(ingrediant)