from BotEngine.Editor.BotClass import *
import pickle

class Editor():

    def createBot(self, name, token):

        if(name == ''):
            name = input('Enter bot name: ')

        if(token == ''):
            token = input('Enter bot token: ')

        self.CurrentBot = ChatBot(name, token) # Creating bot

        self.saveBot(self.CurrentBot) # Saving bot



    def loadBot(self, name):

        BotFile = open('../Bots/' + name, 'rb+')

        self.CurrentBot = pickle.load(BotFile)

        print(self.CurrentBot.Name)

        BotFile.close() # Closes file


    def saveBot(self, bot):

        BotFile = open('../Bots/' + bot.Name, 'wb+') # Create or Open File

        BotFile.truncate() # Clear File
        pickle.dump(bot, BotFile, protocol=pickle.HIGHEST_PROTOCOL) # Write Bot Class

        BotFile.close() # Close file



app = Editor()
#app.createBot('','')
app.loadBot('A')
print(app.CurrentBot.Name + 'len(app.CurrentBot.bot_blueprints)')
app.CurrentBot.addBlueprint()
app.saveBot(app.CurrentBot)
print(len(app.CurrentBot.bot_blueprints))
