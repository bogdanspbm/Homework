from BotEngine.Editor.FuncLabClass import *


class Blueprint():

    def __init__(self, id, name, parent, bot):

        self.ID = id
        self.name = name
        self.blueprint_lib = {
        }
        self.global_vars = bot.global_vars
        self.funcs = []
        self.ParentBot = parent

    def closeBlueprint(self):

        self.ParentBot.botMenu(self.ParentBot.Parent)

    def addFunc(self, type='', inputv='', output='', goto=-1):

        if inputv == '':
            inputv = input('Enter input: ')

        if type == '':
            type = input('Enter type: ')

        if output == '':
            output = input('Enter output: ')

        if goto == -1 and type != 'print':
            goto = int(input('Enter goto: '))

        fc = BlueprintFunctions(type, inputv, output, goto, self)
        self.funcs.append(fc)

        return fc

    def display_funcs(self):

        for func in self.funcs:
            print(func.input)

    def find_func_by_output(self, output):

        for func in self.funcs:
            if func.output == output:
                return func

        return -1

    def find_output_by_input(self, input):
        for func in self.funcs:
            if func.try_to_input(input) != 0:
                return func.try_to_input(input)

    def testBluerpint(self):
        while True:
            inp = input('Test: ')

            if inp == 'stop':
                return

            self.find_output_by_input(inp)

    def bpEditor(self, parentBot):

        actions = {
            'add': self.addFunc,
            'close': self.closeBlueprint,
            'test': self.testBluerpint,
            'funcs': self.display_funcs
        }

        # self.ParentBot = parentBot

        while True:
            actions[input('Blueprint: ')]()
