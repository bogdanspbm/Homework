import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton


class Child(tk.Toplevel):
    def __init__(self, root, bot):
        super().__init__(root)
        self.root = root
        self.bot = bot
        self.tmpname = self.bot.Name
        self.button_image = tk.PhotoImage(file='../Sprites/ButtonL_0.png')
        self.bg = tk.PhotoImage(file='../Sprites/bot_settings.png')
        self.init_child()

    def init_child(self):
        self.title('Create Bot')
        self.geometry('400x600+700+50')
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=400, height=600, bd=0,
                                highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        image2 = self.canvas.create_image(200, 300, image=self.bg)
        image1 = self.canvas.create_image(367, 586, image=self.button_image,
                                          tag='ok')
        self.canvas.tag_bind('ok', '<Button-1>', self.update_bot)

        self.bot_name = tk.Entry(self.canvas, bg='#dedede', bd=0,
                                 highlightthickness=0, width=15)
        self.bot_name.place(x=126, y=30)
        self.bot_name.insert(tk.END, self.bot.Name)

        self.vk_token = tk.Entry(self.canvas, bg='#dedede', bd=0,
                                 highlightthickness=0, width=25)
        self.vk_token.place(x=57, y=65)
        self.vk_token.insert(tk.END, self.bot.vk_token)

        self.tel_token = tk.Entry(self.canvas, bg='#dedede', bd=0,
                                  highlightthickness=0, width=25)
        self.tel_token.place(x=57, y=99)
        self.tel_token.insert(tk.END, self.bot.tel_token)

    def update_bot(self, event=''):
        self.bot.Name = self.bot_name.get()
        self.bot.vk_token = self.vk_token.get()
        self.bot.tel_token = self.tel_token.get()
        self.root.engine.del_bot(self.tmpname)
        self.root.save_bot()
        self.root.last_bot_name = self.bot.Name
        self.root.cur_bot_name = self.bot.Name
        self.root.update_combobox()
        self.destroy()
