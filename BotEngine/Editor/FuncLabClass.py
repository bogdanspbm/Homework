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
        self.parent.ParentBot.save_local_bot()

    def get_all_splits(self, input):

        arr = input.split('%')
        return arr

    def find_overlap(self, first, second):
        last_right = ''
        try:
            for i in range(len(first)):
                test1, test2 = first[i:], second[:len(first) - i]
                if test1 == test2:
                    last_right = test1
            return last_right
        except:
            return last_right

    def try_to_write_var(self, myinput, funcinput):

        splits = (funcinput + '.').split('%')

        myinp = myinput

        my_dic = {}

        first_eq = []
        sec_eq = []

        new_keys = []
        new_vals = []

        flag = 0

        for i in range(len(splits) - 2):
            if i % 2 == 0:
                a = myinp.split(splits[i + 2])
                if a[0] == '':
                    a.remove('')
                b = myinp.split(splits[i])
                if b[0] == '':
                    b.remove('')
                val = self.find_overlap(a[0], b[len(b) - 1])  # NADO FIXIT'
                if val != '':
                    new_keys.append(splits[i + 1])
                    new_vals.append(val)
                    my_dic[splits[i + 1]] = val

        tmp_out = funcinput

        for key in my_dic:
            tmp_out = tmp_out.replace('%' + str(key) + '%', str(my_dic[key]))

        if tmp_out == myinput:
            for i in range(len(new_keys)):
                self.add_global_var(new_keys[i], new_vals[i])
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
            try:
                self.secoutput = self.secoutput.replace('%' + str(key) + '%',
                                                        str(self.global_vars[
                                                                key]()))
            except:
                self.secoutput = self.secoutput.replace('%' + str(key) + '%',
                                                        str(self.global_vars[
                                                                key]))
        return self.secoutput

    def printMessageAndGoTo(self):

        print(self.ouptut)
        self.parent.ParentBot.selectCurrentBP(self.goto)

    def try_to_input(self, input):

        if self.type == 'print':

            for i in self.input.split(';'):
                if i == input:
                    self.result(self)
                    return self.upgrade_output()
                elif i.count('%') > 1 and self.try_to_write_var(input, i) == 1:
                    return self.upgrade_output()
            return 0

        if self.type == 'printgoto':
            for i in self.input.split(';'):
                if i == input:
                    self.result(self)
                    return self.upgrade_output()
                elif i.count('%') > 1 and self.try_to_write_var(input, i) == 1:
                    self.parent.ParentBot.CurrentBP = self.goto
                    return self.upgrade_output()
            return 0

    funcs = {
        'print': printMessage,
        'printgoto': printMessageAndGoTo
    }
