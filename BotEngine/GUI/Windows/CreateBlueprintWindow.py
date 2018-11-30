import tkinter as tk
from tkinter import ttk


class Child(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.enter_name = -1
        self.btn_enter = -1
        self.init_child()

    def init_child(self):
        self.title('Create Blueprint')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        label_desc = tk.Label(self, text='Enter Blueprint Name')
        label_desc.place(x=50, y=50)

        self.enter_name = ttk.Entry(self)
        self.enter_name.place(x=200, y=50)

        self.btn_enter = ttk.Button(self, text='Accept',
                                    command=self.create_bp)
        self.btn_enter.place(x=100, y=80)

        # self.grab_set()
        self.focus_set()

    def create_bp(self):
        self.root.engine.CurrentBot.addBlueprint(self.enter_name.get(),
                                                 self.root.engine)
        self.root.update_bp()
        self.destroy()