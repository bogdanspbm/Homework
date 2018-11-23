import tkinter as tk
from tkinter import ttk
from BotEngine.GUI import CreateBotWindow as cw
from BotEngine.GUI import BotIcon as bc
import os

class BlueprintItem:

    def __init__(self, root, id):
        self.id = id
        self.root = root
        self.frame = ttk.Button(root.editor_bar, text=id, command=self.load_bp)
        self.frame.pack(side=tk.TOP, fill=tk.X)

    def load_bp(self):
        self.root.engine.CurrentBot.selectCurrentBP(self.id)
