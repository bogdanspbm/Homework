import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton


class BlueprintItem:
    def __init__(self, root, id, name):
        self.id = id
        self.name = name
        self.root = root
        self.image = root.bp_image
        self.cross_image = root.cross_image
        x0 = 134
        y0 = 76
        x = self.image.width()
        y = self.image.height()

        root.canvas.create_image(x0 + (x + 10) * (root.last_row % 3),
                                 y0 + (y + 10) * int(root.last_row / 3),
                                 image=self.image,
                                 tag=('bp' + str(root.last_row)))

        root.canvas.tag_bind('bp' + str(root.last_row), '<Button-1>',
                             self.load_bp)

        root.canvas_tags.append('bp' + str(root.last_row))

        root.canvas.create_text(x0 + (x + 10) * (root.last_row % 3) - 78,
                                y0 + (y + 10) * int(root.last_row / 3) - 48,
                                font=("Bebas Bold", 20), text=self.name,
                                tag=('txt' + str(root.last_row)))

        root.canvas_tags.append(('txt' + str(root.last_row)))

        root.canvas.create_image(x0 + (x + 10) * (root.last_row % 3) + 106,
                                 y0 + (y + 10) * int(root.last_row / 3) - 48,
                                 image=self.cross_image,
                                 tag=('cross' + str(root.last_row)))

        root.canvas.tag_bind('cross' + str(root.last_row), '<Button-1>',
                             self.del_bp)

        root.canvas_tags.append('cross' + str(root.last_row))

        root.last_row += 1

    def load_bp(self, event=''):
        self.root.cur_bp = self.id
        self.root.engine.CurrentBot.selectCurrentBP(self.id)
        self.root.fill_funcs()

    def del_bp(self, event=''):
        self.root.engine.CurrentBot.bot_blueprints.pop(self.id)
        self.root.save_bot()
        self.root.select_bot()
        pass