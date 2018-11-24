import tkinter as tk
from tkinter import ttk


class Child(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.enter_name = -1
        self.type = -1
        self.btn_enter = -1
        self.init_child()

    def init_child(self):
        type_list = ['Print', 'PrintGoto']

        self.title('Create Blueprint')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.enter_output = ttk.Entry(self)
        self.enter_output.place(x=30, y=20)

        self.enter_input = ttk.Entry(self)
        self.enter_input.place(x=30, y=50)

        self.type_box = ttk.Combobox(self, values=type_list)
        self.type_box.place(x=30, y=80)
        self.type_box.current(0)

        self.btn_enter = ttk.Button(self, text='Accept', command=self.save_change)
        self.btn_enter.place(x=30, y=130)

        self.grab_set()
        self.focus_set()

    def save_change(self):
        #self.root.engine.CurrentBot.addBlueprint(self.enter_name.get())
        #self.root.update_bp()
        self.destroy()
