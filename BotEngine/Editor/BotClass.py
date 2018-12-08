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
        self.cur_bp = {}
        self.users_id = []
        self.global_vars = {
            'H': self.get_hour,
            'MIN': self.get_minute,
            'S': self.get_sec,
            'D': self.get_day,
            'MONTH': self.get_month,
            'Y': self.get_year,
            'WD': self.get_week_day
        }

    def add_id(self, id):
        self.users_id.append(id)
        self.cur_bp[id] = 0
        self.save_local_bot()

    def get_hour(self):
        return time.datetime.now().hour

    def get_minute(self):
        return time.datetime.now().minute

    def get_sec(self):
        return time.datetime.now().second

    def get_day(self):
        return time.datetime.now().day

    def get_month(self):
        return time.datetime.now().month

    def get_year(self):
        return time.datetime.now().year

    def get_week_day(self):
        return time.datetime.weekday()

    def selectCurrentBP(self, bp=-1, id=-1):

        if bp == -1:
            bp = int(input('Enter BP id: '))

        self.CurrentBP = bp
        self.cur_bp[id] = bp
        self.bot_blueprints[bp].enter_event(id)
        self.save_local_bot()

    def select_bp_with_name(self, name):
        for i in range(len(self.bot_blueprints)):
            if self.bot_blueprints[i].name == name:
                print(name + ' ' + self.bot_blueprints[i].name)

    def get_bp_index_by_name(self, name):
        for i in range(len(self.bot_blueprints)):
            if self.bot_blueprints[i].name == name:
                return i

    def addBlueprint(self, name='', root=-1):
        self.bot_blueprints.append(Blueprint(len(self.bot_blueprints), name,
                                             self.Parent,
                                             self))  # Add clear blueprint to list
        print(len(self.bot_blueprints))

        if root != -1:
            self.saveBot(root)

    @staticmethod
    def closeBot(root):
        root.editorMenu()

    @staticmethod
    def saveBot(root):

        root.saveBot()

    def save_local_bot(self):
        BotFile = open('../Bots/' + self.Name + '.bot',
                       'wb+')  # Create or Open File

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
