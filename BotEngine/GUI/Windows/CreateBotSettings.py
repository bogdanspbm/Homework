import tkinter as tk
from tkinter import ttk


class Child(tk.Toplevel):
    def __init__(self, root, bot):
        super().__init__(root)
        self.root = root
        self.bot = bot
        self.init_child()

    def init_child(self):
        self.title('Create Bot')
        self.geometry('700x400+400+300')
        self.resizable(False, False)

        label_desc = tk.Label(self, text='Bot Name:')
        label_desc.grid(row=0,column=0)

        self.enter_name = ttk.Entry(self)
        self.enter_name.insert(tk.END, self.bot.Name)
        self.enter_name.grid(row=0,column=1)

        self.btn_enter = ttk.Button(self, text='Accept',
                                    command=self.create_bot)
        self.btn_enter.grid(row=1,column=0)

        # self.grab_set()
        self.focus_set()

    def create_bot(self):
        self.root.engine.createBot(self.enter_name.get(), 'TOKEN')
        self.root.update_combobox()
        self.destroy()
