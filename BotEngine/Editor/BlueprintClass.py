from BotEngine.Editor.FuncLabClass import *

class Blueprint():

    def __init__(self, id, name, parent):

        self.ID = id
        self.name = name
        self.blueprint_lib = {
    }
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

        if inputv[len(inputv) - 2] != ';':
            inputv += ';'

        if inputv[len(inputv) - 2] != ';':
            inputv += ';'

        words = inputv.split(';')

        print(words)

        for i in range(len(words)):

                flag = 0

                if i < len(words) - 1 and len(words[i]) > 0:
                    if words[i][len(words[i]) - 1] == '%' and words[i + 1][0] == '%':
                        word = words[i] + ';' + words[i+1]
                        flag = 1

                if i > 0 and len(words[i-1]) > 0:
                    if words[i-1][len(words[i-1]) - 1] == '%' and words[i][0] == '%':
                        word = words[i-1] + ';' + words[i]
                        flag = 1



                if flag == 0:
                    word = words[i]

                word = word.replace('%;%', ';')

                print(word)
                self.blueprint_lib[word] = BlueprintFunctions(type, word, output, goto, self)




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

