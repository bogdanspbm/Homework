import tkinter as tk
from tkinter import ttk
from BotEngine.GUI import CreateBotWindow as cw
from BotEngine.GUI import CreateBlueprintWindow as cbp
from BotEngine.GUI import EditFuncWindow as efw
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

        button_add_bp = ttk.Button(self.editor_bar, text='Add Blueprint', command=self.create_bp)
        button_add_bp.pack(side=tk.BOTTOM)

        button_del_bot = ttk.Button(self.editor_bar, text='Delete Bot', command=self.delete_bot)
        button_del_bot.pack(side=tk.BOTTOM)

    def delete_bot(self):
        self.engine.delete_cur_bot()

        self.update_combobox()

    def del_bp(self):
        pass

    def add_func(self):
        efw.Child(self)


    def fill_funcs(self):

        self.editor_bar.destroy()

        self.editor_bar = tk.Frame(bg='#DDDDDD', width=300)
        self.editor_bar.pack(side=tk.LEFT, fill=tk.BOTH)

        button_back = ttk.Button(self.editor_bar, text='Back', command=self.select_bot)
        button_back.pack(side=tk.BOTTOM)

        button_add_func = ttk.Button(self.editor_bar, text='Add Func', command=self.add_func)
        button_add_func.pack(side=tk.BOTTOM)

        button_del_bp = ttk.Button(self.editor_bar, text='Delete Func', command=self.del_bp)
        button_del_bp.pack(side=tk.BOTTOM)




    def fill_blueprint(self):

        self.bp_arr = []

        for bp in range(len(self.engine.CurrentBot.bot_blueprints)):
            bot = self.engine.CurrentBot.bot_blueprints[bp]
            self.bp_arr.append(blc.BlueprintItem(self, bp, bot.name))
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
        cw.Child(self)  # Spawn create bot menu

    def create_bp(self):
        cbp.Child(self)  # Spawn create bp menu

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

