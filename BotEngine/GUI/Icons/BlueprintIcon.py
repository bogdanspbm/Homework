import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton


class BlueprintItem:
    def __init__(self, root, id, name):
        self.id = id
        self.name = name
        self.root = root
        self.image = tk.PhotoImage(file='../Sprites/BP_Test.png')
        self.image2 = tk.PhotoImage(file='../Sprites/BP_Test_2.png')
        self.frame = MyButton(root.rows[root.last_row %3],image1=self.image,image2=self.image2, mytext=name, mycommand=self.load_bp, mybg='#eeeeee')
        root.last_row+=1
        self.frame.pack(side=tk.TOP, padx=2,pady=2)

    def load_bp(self):
        self.root.cur_bp = self.id
        self.root.engine.CurrentBot.selectCurrentBP(self.id)
        self.root.fill_funcs()
