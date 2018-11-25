from BotEngine.Editor.FuncLabClass import *

class Blueprint():

    def __init__(self, id, name, parent):

        self.ID = id
        self.name = name
        self.blueprint_lib = {
    }
        self.funcs = []
        self.ParentBot = parent

    def closeBlueprint(self):

        self.ParentBot.botMenu(self.ParentBot.Parent)

    def addFunc(self, type = '', inputv = '', output = '', goto = -1):

        if inputv == '':
            inputv = input('Enter input: ')

        if type == '':
            type = input('Enter type: ')

        if output == '':
            output = input('Enter output: ')

        if goto == -1 and type != 'print':
            goto = int(input('Enter goto: '))

        self.funcs.append(BlueprintFunctions(type, inputv, output, goto))

    def find_func_by_output(self, output):

        for func in self.funcs:
            if func.output == output:
                return func

        return -1

    def find_output_by_input(self, input):
        for func in self.funcs:
            if func.try_to_input(input):
                return 1

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
        'test': self.testBluerpint
        }

        #self.ParentBot = parentBot

        while True:
            actions[input('Blueprint: ')]()

