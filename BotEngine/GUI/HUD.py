import tkinter as tk
from tkinter import ttk
from BotEngine.GUI import CreateBotWindow as cw
from BotEngine.GUI import BotIcon as boc
from BotEngine.GUI import BlueprintIcon as blc
import os

class Main(tk.Frame):

    def __init__(self, root, engine):
        super().__init__(root)
        self.parent = root
        self.bots_arr = []
        self.bp_arr = []
        self.engine = engine

        self.init_main()

    def init_main(self):
        self.toolbar = tk.Frame(bg='#aaaaaa', width = 200, bd=2)
        #self.toolbar.grid(column=0)
        self.toolbar.pack(side=tk.LEFT, fill=tk.Y)

        self.editor_bar = tk.Frame(bg='#DDDDDD', width=300)
        #self.editor_bar.grid(column=1)
        self.editor_bar.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scroll = ttk.Scrollbar(self.toolbar)
        self.scroll.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.fill_bot_bar()

        self.init_menu()

    def init_menu(self):
        self.parent.title("Simple menu")

        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Create bot", command=self.create_bot)
        fileMenu.add_command(label="Save bot", command=self.save_bot)
        fileMenu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="Editor", menu=fileMenu)

    def select_bot(self):

        self.editor_bar.destroy()

        self.editor_bar = tk.Frame(bg='#DDDDDD', width=300)
        self.editor_bar.pack(side=tk.LEFT, fill=tk.BOTH)

        self.spawn_editor_menu()
        self.fill_blueprint()


    def spawn_editor_menu(self):

        button_add_bp = ttk.Button(self.editor_bar, text='Add Blueprint', command = self.add_bp)
        button_add_bp.pack(side=tk.BOTTOM)



    def fill_blueprint(self):

        self.bp_arr = []

        for bp in range(len(self.engine.CurrentBot.bot_blueprints)):
            self.bp_arr.append(blc.BlueprintItem(self, bp))
            print(bp)

        print(len(self.engine.CurrentBot.bot_blueprints))



    def update_bp(self):

        for bp in self.bp_arr:
            bp.frame.destroy()

        self.fill_blueprint()


    def add_bp(self):
        self.engine.CurrentBot.addBlueprint()
        self.update_bp()


    def on_exit(self):
        self.quit()

    def create_bot(self):
        cw.Child(self)

    def save_bot(self):
        self.engine.saveBot()
        pass

    def fill_bot_bar(self):

        for bot in os.listdir('../Bots'):
            self.bots_arr.append(boc.BotItem(self, bot))


    def update_combobox(self):

        for bot in self.bots_arr:
            bot.frame.destroy()

        self.fill_bot_bar()




class BotEditor(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.init_child()

    def init_child(self):
        self.geometry('400x200+400+300')
        pass

