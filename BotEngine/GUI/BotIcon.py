import tkinter as tk
from tkinter import ttk
from BotEngine.GUI import CreateBotWindow as cw
from BotEngine.GUI import BotIcon as bc
import os

class BotItem:

    def __init__(self, root, name):
        self.name = name
        self.root = root
        root.button = ttk.Button(root.scroll, text=name, command=self.load_bot)
        root.button.pack(side=tk.TOP, fill=tk.X)

    def load_bot(self):
        self.root.engine.loadBot(self.name)
        self.root.select_bot()


