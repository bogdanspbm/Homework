import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton



class FuncItem:
    def __init__(self, root, func):
        self.func = func
        self.root = root
        self.image = tk.PhotoImage(file='../Sprites/TestButton.png')
        self.image2 = tk.PhotoImage(file='../Sprites/TestButton_2.png')
        self.frame = MyButton(root.bot_columns, image1=self.image, image2=self.image2, mytext=func.output, mycommand=self.edit_func,
                              mybg='#eeeeee')
        root.last_row+=1
        self.frame.pack(side=tk.TOP, fill=tk.X, padx=0, pady=0)

    def edit_func(self):
        self.root.add_func(self.func)
        pass
