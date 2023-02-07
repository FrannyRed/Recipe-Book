class RecipeInstructions:

    def __init__(self):
        self.instructions = []

    # iterate over list of instructions and display them to the user
    def list_instructions(self):
        for step in range(len(self.instructions)):
            print(f'Step {step+1}: {self.instructions[step]}')

    # add an instruction to the instructions list
    def add_instructions(self):
        print('======== Add Instructions ========')
        new_instructions = input('Input Here: ')
        self.instructions.append(new_instructions)

    # change an existing instruction step
    def change_instructions(self, choice):
        choice = choice - 1
        print('Current Instructions:')
        print(f'{self.instructions[choice]}')
        print('Input New Instructions:')
        new_instructions = input('Instructions: ')
        self.instructions[choice] = new_instructions

    # change an existing instruction step
    def delete_instructions(self, choice):
        choice = choice - 1
        del self.instructions[choice]