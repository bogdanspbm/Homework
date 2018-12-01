import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton


class BotItem:
    def __init__(self, root, name):
        self.name = name
        self.root = root
        self.image = tk.PhotoImage(file='../Sprites/TestButton.png')
        self.image2 = tk.PhotoImage(file='../Sprites/TestButton_2.png')
        self.frame = MyButton(root.toolbar,image1=self.image,image2=self.image2, mytext=name, mycommand=self.load_bot, mybg='#eeeeee')
        self.frame.pack(side=tk.TOP, fill=tk.X,padx=0,pady=0)

    def load_bot(self):
        self.root.engine.loadBot(self.name)
        self.root.select_bot()
