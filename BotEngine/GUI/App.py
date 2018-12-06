import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.Windows import CreateBlueprintWindow as cbp, \
    CreateBotWindow as cw, EditFuncWindow as efw, CreateBotSettings as cbs
from BotEngine.GUI.Icons import BotIcon as boc, BlueprintIcon as blc, \
    FunctionIcon as fuc
from BotEngine.Editor.FuncLabClass import BlueprintFunctions
import os
from BotEngine.BotsAPI.Telegram.Bot import TelegramBot
from BotEngine.BotsAPI.VK.Bot import VKBot


class Main(tk.Frame):

    def __init__(self, root, engine):
        super().__init__(root)
        self.parent = root
        self.tel_bots_treads = {}
        self.vk_bots_treads = {}
        self.load_sprites()
        self.bots_arr = []
        self.bp_arr = []
        self.fc_arr = []
        self.tel_bots = []
        self.vk_bots = []
        self.threads = []
        self.canvas_tags = []
        self.cur_bp = -1
        self.tabs = []
        self.cur_bot_name = -1
        self.cur_bot = None
        self.columns = 3
        self.last_row = 0
        self.engine = engine
        self.last_bot_button = None
        self.last_bot_name = ''
        self.editor_bar = None
        self.current_state = 0

        self.init_main()

    def clear_canvas(self):
        for tag in self.canvas_tags:
            self.canvas.delete(tag)

        self.canvas_tags = []

    def load_sprites(self):
        self.toolbar_image = tk.PhotoImage(file='../Sprites/tool_bar.png')
        self.add_image = tk.PhotoImage(file='../Sprites/plus.png')
        self.remove_image = tk.PhotoImage(file='../Sprites/unchecked.png')
        self.teloff = tk.PhotoImage(file='../Sprites/teloff.png')
        self.telon = tk.PhotoImage(file='../Sprites/telon.png')
        self.vkoff = tk.PhotoImage(file='../Sprites/vkoff.png')
        self.vkon = tk.PhotoImage(file='../Sprites/vkon.png')
        self.editor_image = tk.PhotoImage(file='../Sprites/Editor_Bar.png')
        self.bp_image = tk.PhotoImage(file='../Sprites/BP_Bar.png')
        self.back_image = tk.PhotoImage(file='../Sprites/back.png')
        self.invisible_image = tk.PhotoImage(
            file='../Sprites/invisiblebox.png')
        self.cross_image = tk.PhotoImage(
            file='../Sprites/cross.png')

    def init_main(self):

        self.init_tab()

        self.toolbar = tk.Label(bg='#eeeeee', bd=0, highlightthickness=0)
        self.toolbar.pack(side=tk.LEFT, fill=tk.Y, padx=0, pady=0)

        self.init_editor_bar()

        self.fill_bot_bar()

        self.init_menu()

    def init_tab(self):

        xc = self.toolbar_image.width()
        yc = self.toolbar_image.height()

        self.tab = tk.Canvas(width=xc, height=yc, bd=0, highlightthickness=0)
        self.tab.pack(side=tk.BOTTOM, fill=tk.X)

        bg = self.tab.create_image(xc / 2, yc / 2, image=self.toolbar_image,
                                   tag='bg')

        invisible = self.tab.create_image(0, yc / 2,
                                          image=self.invisible_image)

    def init_editor_bar(self):

        if self.editor_bar != None:
            self.clear_canvas()

        self.editor_bar = tk.Frame(bd=0, highlightthickness=0)
        self.editor_bar.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.scroll = tk.Scrollbar(self.editor_bar, bd=0, highlightthickness=0)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(self.editor_bar, width=500, height=2000,
                                bg='#dddddd', bd=0, highlightthickness=0,
                                scrollregion=(0, 0, 2000, 2000))

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.canvas.yview)

    def destroy_tab_icons(self):
        for tab in self.tabs:
            self.tab.delete(tab)

        self.tabs = []

    def init_bp_tab(self):

        xc = self.toolbar_image.width()
        yc = self.toolbar_image.height()

        if self.current_state != -1:

            if self.vk_bots.count(self.cur_bot_name) != 0:
                vk_image = self.vkon
            else:
                vk_image = self.vkoff

            if self.tel_bots.count(self.cur_bot_name) != 0:
                tel_image = self.telon
            else:
                tel_image = self.teloff

            self.destroy_tab_icons()
            self.current_state = 1

            self.tab.create_image(984, yc / 2, image=self.add_image, tag='add')
            self.tab.tag_bind('add', '<Button-1>', self.create_bp)

            self.tab.create_image(16, yc / 2, image=self.remove_image,
                                  tag='remove')
            self.tab.tag_bind('remove', '<Button-1>', self.delete_bot)

            self.tel_img_id = self.tab.create_image(64, yc / 2,
                                                    image=tel_image,
                                                    tag='run_tel')
            self.tab.tag_bind('run_tel', '<Button-1>', self.run_tel_bot)

            self.vk_img_id = self.tab.create_image(110, yc / 2,
                                                   image=vk_image,
                                                   tag='run_vk')
            self.tab.tag_bind('run_vk', '<Button-1>', self.run_vk_bot)

            self.tabs.append('add')
            self.tabs.append('remove')
            self.tabs.append('run_tel')
            self.tabs.append('run_vk')

    def init_func_tab(self):

        xc = self.toolbar_image.width()
        yc = self.toolbar_image.height()

        if self.current_state != 2:
            self.destroy_tab_icons()
            self.current_state = 2

            self.tab.create_image(984, yc / 2, image=self.add_image, tag='add')
            self.tab.tag_bind('add', '<Button-1>', self.add_func)

            self.tab.create_image(16, yc / 2, image=self.remove_image,
                                  tag='remove')
            self.tab.tag_bind('remove', '<Button-1>', self.delete_bot)

            self.tab.create_image(40, yc / 2, image=self.back_image,
                                  tag='back')
            self.tab.tag_bind('back', '<Button-1>', self.select_bot)

            self.tabs.append('add')
            self.tabs.append('remove')
            self.tabs.append('back')

    def init_menu(self):
        self.parent.title("Simple menu")

        menubar = tk.Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Create bot", command=self.create_bot)
        fileMenu.add_command(label="Save bot", command=self.save_bot)
        fileMenu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="Editor", menu=fileMenu)

        if self.engine.CurrentBot != -1:
            fileBot = tk.Menu(menubar)
            fileBot.add_command(label="Settings", command=self.bot_settings)
            menubar.add_cascade(label="Bot", menu=fileBot)

    def select_bot(self, event=''):

        self.cur_bot = self.engine.CurrentBot

        self.clear_canvas()
        self.init_bp_tab()

        self.fill_blueprint()
        self.init_menu()

    def delete_bot(self, event=''):
        self.current_state = 0
        self.last_bot_name = ''
        self.cur_bot_name = ''
        self.last_bot_button = None
        self.engine.delete_cur_bot()
        self.update_combobox()
        self.clear_canvas()
        self.destroy_tab_icons()
        self.init_menu()

    def del_bp(self):
        pass

    def add_func(self, event='', func=-1):
        if func == -1:
            func = BlueprintFunctions(parentbp=self.cur_bot.bot_blueprints[self.cur_bp])
            self.engine.CurrentBot.bot_blueprints[self.cur_bp].funcs.append(
                func)

        efw.Child(self, func)

    def update_func(self):

        self.clear_canvas()

        self.last_row = 0

        self.fc_arr = []
        id = self.cur_bp

        for fc in range(len(self.engine.CurrentBot.bot_blueprints[id].funcs)):
            func = self.engine.CurrentBot.bot_blueprints[id].funcs[fc]
            self.fc_arr.append(fuc.FuncItem(self, func))

    def fill_blueprint(self):

        self.last_row = 0

        self.bp_arr = []

        for bp in range(len(self.engine.CurrentBot.bot_blueprints)):
            bot = self.engine.CurrentBot.bot_blueprints[bp]
            self.bp_arr.append(blc.BlueprintItem(self, bp, bot.name))

    def fill_funcs(self):

        self.last_row = 0

        self.clear_canvas()
        self.init_func_tab()

        self.update_func()

    def update_bp(self):

        self.clear_canvas()

        self.fill_blueprint()

    def add_bp(self):
        self.engine.CurrentBot.addBlueprint()
        self.update_bp()

    def on_exit(self):
        self.quit()

    def create_bot(self):
        cw.Child(self)  # Spawn create bot menu

    def create_bp(self, event=''):
        cbp.Child(self)  # Spawn create bp menu

    def save_bot(self):
        self.engine.saveBot()
        pass

    def bot_settings(self):
        cbs.Child(self, self.engine.CurrentBot)
        pass

    def run_tel_bot(self, event=''):
        if self.tel_bots.count(self.cur_bot_name) == 0:
            self.tel_bots.append(self.cur_bot_name)
            self.save_bot()
            self.tab.itemconfigure(self.tel_img_id, image=self.telon)
            bot = TelegramBot(self.engine.CurrentBot)
            self.tel_bots_treads[self.cur_bot_name] = bot
            self.threads.append(bot)
            bot.start()
        else:
            self.tel_bots.remove(self.cur_bot_name)
            self.tel_bots_treads[self.cur_bot_name].active=False
            self.save_bot()
            self.tab.itemconfigure(self.tel_img_id, image=self.teloff)

    def run_vk_bot(self, event=''):
        if self.vk_bots.count(self.cur_bot_name) == 0:
            self.vk_bots.append(self.cur_bot_name)
            self.save_bot()
            self.tab.itemconfigure(self.vk_img_id, image=self.vkon)
            bot = VKBot(self.engine.CurrentBot)
            self.vk_bots_treads[self.cur_bot_name] = bot
            self.threads.append(bot)
            bot.start()
        else:
            self.vk_bots.remove(self.cur_bot_name)
            self.vk_bots_treads[self.cur_bot_name].active=False
            self.save_bot()
            self.tab.itemconfigure(self.vk_img_id, image=self.vkoff)

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
