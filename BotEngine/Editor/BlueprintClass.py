from BotEngine.Editor.FuncLabClass import *

class Blueprint():

    def __init__(self, id, parent):
        self.ID = id
        self.blueprint_lib = {
    }
        self.ParentBot = parent

    def closeBlueprint(self):

        self.ParentBot.botMenu(self.ParentBot.Parent)

    def addFunc(self, type = '', inputv = '', output = '', goto = -1):

        if type == '':
            type = input('Enter type: ')

        if inputv == '':
            inputv = input('Enter input: ')

        if output == '':
            output = input('Enter output: ')

        if goto == -1 and type != 'print':
            goto = int(input('Enter goto: '))


        self.blueprint_lib[inputv] = BlueprintFunctions(type, inputv, output, goto, self)


    def testBluerpint(self):
        while True:
            inp = input('Test: ')

            if inp == 'stop':
                return

            self.blueprint_lib[inp].result(self.blueprint_lib[inp])

    def bpEditor(self, parentBot):

        actions = {
        'add': self.addFunc,
        'close': self.closeBlueprint,
        'test': self.testBluerpint
        }

        #self.ParentBot = parentBot

        while True:
            actions[input('Blueprint: ')]()

