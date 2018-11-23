import tkinter as tk
from tkinter import ttk
from BotEngine.GUI import CreateBotWindow as cw
import os


class Child(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.init_child()

    def init_child(self):
        self.title('Create Bot')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.label_desc = tk.Label(self, text='Enter bot Name')
        self.label_desc.place(x=50, y=50)

        self.enter_name = ttk.Entry(self)
        self.enter_name.place(x=200, y=50)

        self.accept_img = tk.PhotoImage(file='../Sprites/Button_accept.png')

        btn_enter = ttk.Button(self, image=self.accept_img, command=self.create_bot)
        btn_enter.place(x=100, y=80)
        #btn_enter.bind('<btn-1>')

        self.grab_set()
        self.focus_set()

    def create_bot(self):
        self.root.engine.createBot(self.enter_name.get(), 'TOKEN')
        self.root.update_combobox()
        self.destroy()