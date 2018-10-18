from BotEngine.Editor.BlueprintClass import *

class ChatBot:

    def __init__(self, Name, Token):
        self.Name = Name
        self.Token = Token
        self.bot_blueprints = []

    def addBlueprint(self):
        self.bot_blueprints.append(Blueprint(len(self.bot_blueprints))) # Add clear blueprint to list
