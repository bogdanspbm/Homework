import tkinter as tk
from tkinter import ttk


class BlueprintItem:
    def __init__(self, root, id, name):
        self.id = id
        self.name = name
        self.root = root
        self.frame = ttk.Button(root.editor_bar, text=name,
                                command=self.load_bp)
        self.frame.pack(side=tk.TOP, fill=tk.X)

    def load_bp(self):
        self.root.cur_bp = self.id
        self.root.engine.CurrentBot.selectCurrentBP(self.id)
        self.root.fill_funcs()
