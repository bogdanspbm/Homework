from BotEngine.Editor.BotClass import *
import pickle
import os


class Editor():

    def __init__(self):
        self.CurrentBot = -1

    def createBot(self, name=''):

        if name == '':
            name = input('Enter bot name: ')

        self.CurrentBot = ChatBot(name)  # Creating bot

        self.saveBot(self.CurrentBot)  # Saving bot

    def delete_cur_bot(self):
        os.remove('../Bots/' + self.CurrentBot.Name)
        self.CurrentBot = -1
        print('Removed')

    def del_bot(self, name):
        os.remove('../Bots/' + name)
        print('Removed')

    def loadBot(self, name=''):

        startname = name

        if name == '':
            name = input('Enter bot name: ')

        BotFile = open('../Bots/' + name, 'rb+')

        bot = pickle.load(BotFile)

        self.CurrentBot = bot

        print(self.CurrentBot.Name)

        BotFile.close()  # Closes file

        self.CurrentBot.Parent = self

        if startname == '':
            self.CurrentBot.botMenu(self)

    def saveBot(self, bot=0):

        if bot == 0:
            bot = self.CurrentBot

        BotFile = open('../Bots/' + bot.Name, 'wb+')  # Create or Open File

        BotFile.truncate()  # Clear File
        pickle.dump(bot, BotFile,
                    protocol=pickle.HIGHEST_PROTOCOL)  # Write Bot Class
        # Write Bot Class

        BotFile.close()  # Close file

    def editorMenu(self):

        actions = {
            'create': self.createBot,
            'load': self.loadBot,
            'save': self.saveBot,
            'exit': exit
        }

        while True:
            actions[input('Editor: ')]()


if __name__ == "__main__":
    app = Editor()
    app.editorMenu()
