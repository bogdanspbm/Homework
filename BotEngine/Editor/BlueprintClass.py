class Blueprint():


    def __init__(self, id):
        self.ID = id
        self.blueprint_lib = {
    }

    def closeBlueprint(self):

        self.ParentBot.botMenu()

    def addNewAnswer(self, type = -1, input = '', output = '', goto = -1):

        if type == -1:
            type = int(input('Enter answer type: '))

        if type == 1:
            pass


    def bpEditor(self, parentBot):

        actions = {

        }

        self.ParentBot = parentBot


        while True:
            actions[input('Blueprint: ')]()

