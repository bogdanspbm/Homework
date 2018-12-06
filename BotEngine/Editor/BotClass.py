from BotEngine.Editor.BlueprintClass import *
import datetime as time
import pickle

class ChatBot:

    def __init__(self, Name):
        self.Name = Name
        self.vk_token = ''
        self.tel_token = ''
        self.bot_blueprints = []
        self.CurrentBP = -1
        self.global_vars = {
            'H': self.get_hour ,
            'M': self.get_minute
        }

    def get_hour(self):
        return time.datetime.now().hour

    def get_minute(self):
        return time.datetime.now().minute

    def selectCurrentBP(self, bp=-1):

        if bp == -1:
            bp = int(input('Enter BP id: '))

        self.CurrentBP = bp

    def addBlueprint(self, name='', root=-1):
        self.bot_blueprints.append(Blueprint(len(self.bot_blueprints), name,
                                             self.Parent,self))  # Add clear blueprint to list
        print(len(self.bot_blueprints))

        if root != -1:
            self.saveBot(root)

    def runBot(self):
        pass

    @staticmethod
    def closeBot(root):
        root.editorMenu()

    @staticmethod
    def saveBot(root):

        root.saveBot()

    def save_local_bot(self):
        BotFile = open('../Bots/' + self.Name + '.bot', 'wb+')  # Create or Open File

        BotFile.truncate()  # Clear File
        pickle.dump(self, BotFile,
                    protocol=pickle.HIGHEST_PROTOCOL)  # Write Bot Class
        # Write Bot Class

        BotFile.close()  # Close file

    def editBlueprint(self, id=0):

        if id == 0:
            id = int(input('Enter ID: '))
            self.bot_blueprints[id].bpEditor(self)

    def displayBlueprints(self):

        print(len(self.bot_blueprints))

    def botMenu(self, ParentEditor):
        actions = {
            'add': self.addBlueprint,
            'run': self.runBot,
            'save': self.saveBot,
            'close': self.closeBot,
            'display': self.displayBlueprints,
            'edit': self.editBlueprint
        }

        self.Parent = ParentEditor

        while True:
            actions[input('Bot: ')]()
