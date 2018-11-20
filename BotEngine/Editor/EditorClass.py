from BotEngine.Editor.BotClass import *
import pickle

class Editor():

    def createBot(self, name = '', token = ''):

        if name == '':
            name = input('Enter bot name: ')

        if token == '':
            token = input('Enter bot token: ')

        self.CurrentBot = ChatBot(name, token) # Creating bot

        self.saveBot(self.CurrentBot) # Saving bot



    def loadBot(self, name = ''):

        if name == '':
            name = input('Enter bot name: ')

        BotFile = open('../Bots/' + name, 'rb+')

        self.CurrentBot = pickle.load(BotFile)

        print(self.CurrentBot.Name)

        BotFile.close() # Closes file

        self.CurrentBot.botMenu(self)


    def saveBot(self, bot = 0):

        if bot == 0:
            bot = self.CurrentBot

        BotFile = open('../Bots/' + bot.Name, 'wb+') # Create or Open File

        BotFile.truncate() # Clear File
        pickle.dump(bot, BotFile, protocol=pickle.HIGHEST_PROTOCOL) # Write Bot Class

        BotFile.close() # Close file

    def editorMenu(self):

        actions = {
        'create': self.createBot,
        'load': self.loadBot,
        'save': self.saveBot
        }

        while True:
            actions[input('Editor: ')]()


if __name__ == "__main__":
    app = Editor()
    app.editorMenu()

