import tkinter as tk
from tkinter import ttk


class FuncItem:
    def __init__(self, root, func):
        self.func = func
        self.root = root
        self.frame = ttk.Button(root.editor_bar, text=func.output,
                                command=self.edit_func)
        self.frame.pack(side=tk.TOP, fill=tk.X)

    def edit_func(self):
        self.root.add_func(self.func)
        pass
