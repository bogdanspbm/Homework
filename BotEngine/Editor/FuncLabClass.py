from BotEngine.Editor.BlueprintClass import *
import time


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
        self.delay = 1
        self.del_flag = None
        self.is_delayed = False
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

    def try_to_write_var(self, myinput, funcinput, id=-1):

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
                    if val.count('_id') > 0:
                        val = val.replace('id', str(id))
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

    def get_new_var(self, input, id=-1):

        status = 0
        var = ''

        for char in input:
            if char == '$' and status == 0:
                status = 1
                var = ''
            if status == 1 and char != '$':
                var.app

    def upgrade_output(self,id=-1):
        self.secoutput = self.output
        for key in self.global_vars.keys():
            try:
                val = str(self.global_vars[key]())
                if val.count('_id') > 0:
                    val = val.replace('id', str(id))
                self.secoutput = self.secoutput.replace('%' + str(key) + '%',
                                                        val)
            except:
                val = str(self.global_vars[key])
                if val.count('_id') > 0:
                    val = val.replace('id', str(id))
                self.secoutput = self.secoutput.replace('%' + str(key) + '%',
                                                        val)
        return self.secoutput

    def printMessageAndGoTo(self):
        self.parent.ParentBot.selectCurrentBP(self.goto)

    def try_to_input(self, input, id=-1):

        if self.type == 'print':

            for i in self.input.split(';'):
                if i == input:
                    self.result(self)
                    return self.upgrade_output(id)
                elif i.count('%') > 1 and self.try_to_write_var(input, i) == 1:
                    return self.upgrade_output(id)
            return None

        if self.type == 'printgoto':
            self.parent.ParentBot.CurrentBP = self.goto
            for i in self.input.split(';'):
                if i == input:
                    self.result(self)
                    return self.upgrade_output(id)
                elif i.count('%') > 1 and self.try_to_write_var(input, i,id) == 1:
                    return self.upgrade_output(id)
            return None

    def calculate_event(self, id=-1):

        try:
            delta = time.process_time() - self.del_flag
        except TypeError:
            delta = 0

        if not self.is_delayed:
            self.del_flag = time.process_time()
            self.is_delayed = True
            print('here ++ ++ + ++ +')

            new = '' + self.input
            new.replace('=', ' ')
            new.replace('>', ' ')
            new.replace('<', ' ')
            new.replace('!', ' ')
            new.replace('not', ' ')
            new.replace('and', ' ')
            keys = new.split(' ')
            try:
                keys = keys.remove('')
            except ValueError:
                pass

            upgrade = '' + self.input
            for key in keys:
                try:
                    upgrade = upgrade.replace(key,
                                              str(self.global_vars[key]()))
                except KeyError:
                    pass
                except:
                    upgrade = upgrade.replace(key, str(self.global_vars[key]))

            if eval(upgrade):
                return self.upgrade_output()

        elif delta >= float(self.delay):
            print('+++')
            self.is_delayed = False
        else:
            print(delta)
            print(self.delay)
            return None

    funcs = {
        'print': printMessage,
        'printgoto': printMessageAndGoTo,
        'event': calculate_event
    }
