import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton


class BlueprintItem:
    def __init__(self, root, id, name):
        self.id = id
        self.name = name
        self.root = root
        self.image = root.bp_image
        x0 = 134
        y0 = 76
        x = self.image.width()
        y = self.image.height()

        root.canvas.create_image(x0 + (x+10) * (root.last_row % 3) ,y0 + (y+10)*int(root.last_row/3),image=self.image,tag=('bp'+str(root.last_row)))
        root.canvas.tag_bind('bp'+str(root.last_row),'<Button-1>',self.load_bp)
        root.last_row+=1

    def load_bp(self,event=''):
        self.root.cur_bp = self.id
        self.root.engine.CurrentBot.selectCurrentBP(self.id)
        self.root.fill_funcs()
