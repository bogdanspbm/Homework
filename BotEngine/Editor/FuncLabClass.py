from BotEngine.Editor.BlueprintClass import *

class BlueprintFunctions():

    def __init__(self, type = '', input = '', output = '', goto = -1, parentbp = 'add bot link'):

        #self.funclink
        self.input = input
        self.output = output

        if type == 'printgoto':
          self.goto = goto

        self.parent = parentbp
        self.result = self.funcs[type]

    def printMessage(self):

        print(self.output)

    def printMessageAndGoTo(self):

        print(self.ouptut)
        self.parent.ParentBot.selectCurrentBP(self.goto)

    funcs = {
        'print': printMessage,
        'printgoto': printMessageAndGoTo
    }

