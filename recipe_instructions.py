from sql_connection import SQLiteConnection

class RecipeInstructions:

    def __init__(self):
        self.instruction_sql = ()
        self.connect = SQLiteConnection()
        self.c = self.connect.cursor()

    # iterate over list of instructions and display them to the user
    def list_instructions(self, name):

        # fetch all instructions for the selected recipe
        self.c.execute("SELECT * FROM recipes WHERE recipe=? AND type='instruction'", (name,))
        items = self.c.fetchall()

        # if there were no instructions, print a message
        # if there is instructions, print them and return the list
        if not items:
            print('No instructions yet...')
        else:
            for item in range(len(items)):
                print(f'Step {item+1}: {items[item][5]}')
            return items

    # add an instruction to the instructions list
    def add_instructions(self, name, date_added):
        
        # ask user for new ingredient
        print('== Input new instruction step ==')
        new_instruction = input('Instruction step: ')

        # input the new ingredient data entry
        self.instruction_sql = (name, date_added,'', 'instruction','', new_instruction)
        sql = ("INSERT INTO recipes VALUES (?, ?, ?, ?, ?, ?)")
        self.c.execute(sql, self.instruction_sql)
        self.connect.commit()

    # change an existing instruction step
    def change_instructions(self, choice, items, name, date_added):
        
        # turn user choice into list location and print the users ingredient choice
        choice = choice-1
        print(f'Current instruction step: {items[choice][5]}')
        print('====================')

        # ask user for new ingredient and update the data entry
        new_instruction = input('New instruction: ')
        sql = """UPDATE recipes SET recipe=?,
                'date added'=?,
                'last cooked'=?,
                type=?,
                step=?,
                details=?
                WHERE recipe=? AND details=? """
        new_instruction = (name, date_added,'', 'instruction','', new_instruction, name, items[choice][5])
        self.c.execute(sql, new_instruction)
        self.connect.commit()

    # change an existing instruction step
    def delete_instructions(self, choice, name, instructions_list):
        choice = choice-1

        # delete the data entry in the database
        sql = ("DELETE FROM recipes WHERE recipe=? AND details=?")
        del_choice = (name, instructions_list[choice][5])
        self.c.execute(sql, del_choice)
        self.connect.commit()