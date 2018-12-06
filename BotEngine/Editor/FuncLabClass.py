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

    def add_global_var(self, var, value):
        self.parent.ParentBot.global_vars[var] = value

    def get_all_splits(self, input):

        arr = input.split('%')
        return arr

    def find_overlap(self,second, first):
        last_right = ''
        try:
            for i in range(len(first)):
                test1, test2 = first[i:], second[:len(s1) - i]
                if test1 == test2:
                    last_right = test1
            return last_right
        except:
            return last_right

    def try_to_write_var(self, myinput, funcinput):

        splits = funcinput + '.'.split('%')

        myinp = myinput + '.'

        first_eq = []
        sec_eq = []

        new_keys = []
        new_vals = []

        flag = 0

        for i in range(len(splits) - 2):
            if i%2 ==0:
                a = myinp.split(splits[i+2])
                b = myinp.split(splits[i])
                val = self.find_overlap(a,b)
                if val != '':
                    new_keys.append(split[i+1])
                    new_vals.append(val)

        for i in range(len(splits)):
            if i % 2 == 1:
                splits.remove(splits[i])

        for val in new_vals:
            myinp.replace(val, '%')

        myinp = myinp.split('%')

        if len(myinp) == len(splits):
            for i in range(len(myinp)):
                if myinp[i] != splits[i]:
                    flag = 1
        else:
            flag = 1

        if flag == 0:
            for i in range(len(new_keys)):
                self.add_global_var(new_keys[i],new_vals[i])
            return 1
        return 0






    def get_new_var(self, input):

        status = 0
        var = ''

        for char in input:
           if char == '$' and status == 0:
               status = 1
               var = ''
           if status == 1 and char != '$':
               var.app

    def upgrade_output(self):
        self.secoutput = self.output
        for key in self.global_vars.keys():
            self.secoutput = self.secoutput.replace('%' + str(key) + '%',
                                                    str(self.global_vars[key]()))
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
            elif self.try_to_write_var(input, i) == 1:
                return self.upgrade_output()
        return 0

    funcs = {
        'print': printMessage,
        'printgoto': printMessageAndGoTo
    }
