import tkinter as tk
from tkinter import ttk


class Child(tk.Toplevel):

    def __init__(self, root, func):
        super().__init__(root)
        self.root = root
        self.enter_name = -1
        self.type = func.type
        self.btn_enter = -1
        self.func = func
        self.init_child()

    def init_child(self):
        type_list = ['print', 'printgoto', 'event']

        self.title('Create Blueprint')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.enter_output = ttk.Entry(self)
        self.enter_output.insert(tk.END, self.func.output)
        self.enter_output.place(x=30, y=20)

        self.enter_input = ttk.Entry(self)
        self.enter_input.insert(tk.END, self.func.input)
        self.enter_input.place(x=30, y=50)

        self.type_box = ttk.Combobox(self, values=type_list)
        self.type_box.current(type_list.index(self.func.type))
        self.type_box.bind("<<ComboboxSelected>>", self.switch_window)
        self.type_box.place(x=30, y=80)

        self.btn_enter = ttk.Button(self, text='Accept',
                                    command=self.save_change)
        self.btn_enter.place(x=30, y=140)

        if self.type == 'printgoto':
            goto_list = []
            for bot in self.func.parent.ParentBot.bot_blueprints:
                goto_list.append(bot.name)
            self.gotobox = ttk.Combobox(self, values=goto_list)
            self.gotobox.current(self.func.goto)
            print(self.func.goto)
            self.gotobox.place(x=30, y=110)

        print(self.type)

        # self.grab_set()
        self.focus_set()

    def switch_window(self, event=''):
        l_type = self.type_box.get()

        if l_type == 'print':
            try:
                self.gotobox.destroy()
            except AttributeError:
                pass
        if l_type == 'printgoto':
            goto_list = []
            for bot in self.func.parent.ParentBot.bot_blueprints:
                goto_list.append(bot.name)
            self.gotobox = ttk.Combobox(self, values=goto_list)
            self.gotobox.current(0)
            self.gotobox.place(x=30, y=110)
            pass
        if l_type == 'event':
            try:
                self.gotobox.destroy()
            except AttributeError:
                pass
    def save_change(self):
        # self.root.engine.CurrentBot.addBlueprint(self.enter_name.get())
        # self.root.update_bp()
        self.func.input = self.enter_input.get()
        self.func.output = self.enter_output.get()
        self.func.type = self.type_box.get()
        self.func.result = self.func.funcs[self.type_box.get()]
        if self.type_box.get() != 'printgoto':
            self.func.goto = -1
        else:
            self.func.goto = self.func.parent.ParentBot.get_bp_index_by_name(
                self.gotobox.get())
            print(self.func.parent.ParentBot.get_bp_index_by_name(
                self.gotobox.get()))
        self.root.update_func()
        self.root.save_bot()
        self.destroy()
