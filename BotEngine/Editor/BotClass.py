from BotEngine.Editor.BlueprintClass import *

class ChatBot:

    def __init__(self, Name, Token):
        self.Name = Name
        self.Token = Token
        self.bot_blueprints = []
        self.CurrentBP = 0
        self.Parent


    def selectCurrentBP(self, bp = -1):

        if bp == -1:
            bp = int(input('Enter BP id: '))

        self.CurrentBP = bp


    def addBlueprint(self):
        self.bot_blueprints.append(Blueprint(len(self.bot_blueprints), self.Parent)) # Add clear blueprint to list

    def runBot(self):
        pass

    def closeBot(self):

        self.Parent.editorMenu()

    def saveBot(self):

        self.Parent.saveBot()

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