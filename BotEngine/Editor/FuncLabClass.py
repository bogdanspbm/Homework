from BotEngine.Editor.BlueprintClass import *
import datetime as time

class BlueprintFunctions():

    def __init__(self, type='print', input='', output='', goto=-1,
                 parentbp='add bot link'):

        self.global_vars = parentbp.global_vars

        # self.funclink
        if input != '':
            self.input = input.translate()
        else:
            self.input = input
        if output != '':
            self.output = output.translate()
        else:
            self.output = output

        self.secoutput = self.output

        self.type = type

        if type == 'printgoto':
            self.goto = goto

        self.parent = parentbp
        self.result = self.funcs[type]

    def printMessage(self):

        print(self.output)


    def upgrade_output(self):
        self.secoutput = self.output
        for key in self.global_vars.keys():
            self.secoutput = self.secoutput.replace('%' + str(key) + '%',
                                              str(self.global_vars[key]))
        return self.secoutput

    def printMessageAndGoTo(self):

        print(self.ouptut)
        self.parent.ParentBot.selectCurrentBP(self.goto)

    def try_to_input(self, input):

        print(time.time().hour)

        for i in self.input.split(';'):
            if i == input:
                self.result(self)
                return self.upgrade_output()
        return 0

    funcs = {
        'print': printMessage,
        'printgoto': printMessageAndGoTo
    }
