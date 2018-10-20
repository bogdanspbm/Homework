import random


class HangmanGame():

    def __init__(self, tryc = 5):
        self.maxtriescount = tryc
        self.words = ['airfield', 'hatchet', 'holidays', 'computer', 'university', 'photoconduction', 'bellwether', 'auxochrome', 'fragmentariness']

    def startNewGame(self):
        self.currentword = self.words[random.randrange(len(self.words))]
        self.currenttry = self.maxtriescount
        self.openedChars = []

    def openChar(self, char):
        if self.currentword.find(char.lower()) != -1:
            self.openedChars.append(char.lower())
            return 1
        else:
            self.currenttry -= 1
            return 0

    def canUseChar(self, char):
        #  useble = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
        useble = 'abcdefghijklmnopqrstuvwxyz'

        if type(char) != str:
            raise TypeError('Need char')

        if useble.find(char.lower()) != -1 and len(char) == 1:
            return 1
        else:
            return 0

    def charToWrite(self, index):
        if self.openedChars.count(self.currentword[index]) != 0:
            return self.currentword[index]
        else:
            return '_'

    def getCurState(self):

        res = ''

        for i in range(len(self.currentword)):
            res += (self.charToWrite(i) + ' ')

        return res

    def checkWin(self):

        res = ''

        for i in range(len(self.currentword)):
            res += (self.charToWrite(i))

        if res == self.currentword:
            return 1
        else:
            return 0

    def checkLose(self):
        return self.currenttry == 0

    def runGame(self):

        self.startNewGame()
        print(self.getCurState())

        while not self.checkWin() and not self.checkLose():

            ch = input('Enter char: ')

            while not self.canUseChar(ch):
                ch = input('Enter char: ')

            self.openChar(ch)

            print('Tries: ' + str(self.currenttry))
            print(self.getCurState())

        if self.checkWin():
            print('You won!')
        else:
            print('You lose(. Secret word = ' + self.currentword)