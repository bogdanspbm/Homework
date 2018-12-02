import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton



class FuncItem:
    def __init__(self, root, func):
        self.func = func
        self.root = root
        self.image = root.bp_image
        x0 = 134
        y0 = 76
        x = self.image.width()
        y = self.image.height()

        root.canvas.create_image(x0 + (x + 10) * (root.last_row % 3), y0 + (y + 10) * int(root.last_row / 3),
                                 image=self.image, tag=('func' + str(root.last_row)))
        root.canvas.tag_bind('func' + str(root.last_row), '<Button-1>', self.edit_func)
        root.canvas_tags.append('func' + str(root.last_row))
        root.last_row += 1

    def edit_func(self,event=''):
        self.root.add_func(func=self.func)


