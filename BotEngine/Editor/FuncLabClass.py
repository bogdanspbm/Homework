from BotEngine.Editor.BlueprintClass import *


class BlueprintFunctions():

    def __init__(self, type='print', input='', output='', goto=-1,
                 parentbp='add bot link'):

        # self.funclink
        if input != '':
            self.input = input.translate()
        else:
            self.input = input
        if output != '':
            self.output = output.translate()
        else:
            self.output = output

        self.type = type

        if type == 'printgoto':
            self.goto = goto

        self.parent = parentbp
        self.result = self.funcs[type]

    def printMessage(self):

        print(self.output)

    def printMessageAndGoTo(self):

        print(self.ouptut)
        self.parent.ParentBot.selectCurrentBP(self.goto)

    def try_to_input(self, input):

        for i in self.input.split(';'):
            if i == input:
                self.result(self)
                return self.output
        return 0

    funcs = {
        'print': printMessage,
        'printgoto': printMessageAndGoTo
    }
