from BotEngine.Editor.BlueprintClass import *

class BlueprintFunctions():

    def __init__(self, input = '', output = '', goto = -1, parentbp = 'add bot link'):
        self.funclink
        self.input = input
        self.output = output
        self.goto = goto
        self.parent = parentbp

    def printMessage(self):

        print(self.output)

    def printMessageAndGoTo(self):

        print(self.ouptut)

