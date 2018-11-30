import tkinter as tk
from tkinter import ttk


class BotItem:
    def __init__(self, root, name):
        self.name = name
        self.root = root
        self.frame = ttk.Button(root.scroll, text=name, command=self.load_bot)
        self.frame.pack(side=tk.TOP, fill=tk.X)

    def load_bot(self):
        self.root.engine.loadBot(self.name)
        self.root.select_bot()
