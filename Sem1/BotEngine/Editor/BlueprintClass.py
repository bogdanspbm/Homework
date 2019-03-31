from BotEngine.Editor.FuncLabClass import *


class Blueprint():

    def __init__(self, id, name, parent, bot):

        self.ID = id
        self.name = name
        self.blueprint_lib = {
        }
        self.global_vars = bot.global_vars
        self.funcs = []
        self.ParentBot = bot

    def closeBlueprint(self):

        self.ParentBot.botMenu(self.ParentBot.Parent)

    def enter_event(self, id=-1):
        for func in self.funcs:
            if func.type == 'event' and func.input == 'enter':
                return func.upgrade_output(id)
            elif func.type == 'event' and func.input == 'entergo':
                self.ParentBot.selectCurrentBP(func.goto, id)
                return func.upgrade_output
        return None

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

    def find_func_by_output(self, output, id=-1):

        for func in self.funcs:
            if func.output == output:
                return func

        return -1

    def find_output_by_input(self, input, id=-1):
        for func in self.funcs:
            res = func.try_to_input(input, id)
            if res != None:
                return res
        return None

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
