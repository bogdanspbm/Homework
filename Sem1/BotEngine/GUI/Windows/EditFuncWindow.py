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
        self.image1 = tk.PhotoImage(file='../Sprites/popup_print_simple.png')
        self.image2 = tk.PhotoImage(file='../Sprites/popup_print.png')
        self.image3 = tk.PhotoImage(file='../Sprites/popup_event.png')
        self.image_bl = tk.PhotoImage(file='../Sprites/ButtonL_0.png')
        self.image_br = tk.PhotoImage(file='../Sprites/ButtonR_0.png')
        self.image_bl_1 = tk.PhotoImage(file='../Sprites/ButtonL.png')
        self.image_br_1 = tk.PhotoImage(file='../Sprites/ButtonR.png')
        self.init_child()

    def init_child(self):
        type_list = ['print', 'printgoto', 'event']

        self.title('Create Blueprint')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        self.window = tk.Canvas(self, width=self.image1.width(),
                                height=self.image1.height(), bd=0,
                                highlightthickness=0)
        self.window.pack(expand=True)
        self.bgimage = self.window.create_image(self.image1.width() / 2,
                                                self.image1.height() / 2,
                                                image=self.image1)
        self.img1 = self.window.create_image(365, 180,
                                             image=self.image_bl,
                                             tag='accept')

        self.window.tag_bind('accept', '<Button-1>', self.save_change)

        self.enter_output = tk.Entry(self, bg='#e7e7e7', bd=0,
                                     highlightthickness=0, width=15)
        self.enter_output.insert(tk.END, self.func.output)
        self.enter_output.place(x=100, y=16)

        self.enter_input = tk.Entry(self, bg='#e7e7e7', bd=0,
                                    highlightthickness=0, width=15)
        self.enter_input.insert(tk.END, self.func.input)
        self.enter_input.place(x=100, y=43)

        self.type_box = ttk.Combobox(self, values=type_list)
        self.type_box.current(type_list.index(self.func.type))
        self.type_box.bind("<<ComboboxSelected>>", self.switch_window)
        self.type_box.place(x=92, y=70)

        if self.type == 'printgoto':
            goto_list = []
            for bot in self.func.parent.ParentBot.bot_blueprints:
                goto_list.append(bot.name)
            self.gotobox = ttk.Combobox(self, values=goto_list)
            self.gotobox.current(self.func.goto)
            print(self.func.goto)
            self.gotobox.place(x=92, y=98)
            self.window.itemconfigure(self.bgimage, image=self.image2)

        if self.type == 'event':
            self.delay_text = tk.Entry(self, bg='#e7e7e7', bd=0,
                                       highlightthickness=0, width=15)
            self.delay_text.insert(tk.END, self.func.delay)
            self.delay_text.place(x=100, y=101)
            self.window.itemconfigure(self.bgimage, image=self.image3)

        # self.grab_set()
        self.focus_set()

    def switch_window(self, event=''):
        l_type = self.type_box.get()

        if l_type == 'print':
            try:
                self.window.itemconfigure(self.bgimage, image=self.image1)
                self.gotobox.destroy()
                self.delay_text.destroy()
            except AttributeError:
                pass
        if l_type == 'printgoto':
            try:
                self.window.itemconfigure(self.bgimage, image=self.image2)
                self.delay_text.destroy()
            except AttributeError:
                pass
            goto_list = []
            for bot in self.func.parent.ParentBot.bot_blueprints:
                goto_list.append(bot.name)
            self.gotobox = ttk.Combobox(self, values=goto_list)
            self.gotobox.current(0)
            self.gotobox.place(x=92, y=98)
            pass
        if l_type == 'event':
            self.window.itemconfigure(self.bgimage, image=self.image3)
            self.delay_text = tk.Entry(self, bg='#e7e7e7', bd=0,
                                       highlightthickness=0, width=15)
            self.delay_text.insert(tk.END, self.func.delay)
            self.delay_text.place(x=100, y=101)
            try:
                self.gotobox.destroy()
            except AttributeError:
                pass

    def save_change(self, event=''):
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

        if self.type_box.get() == 'event':
            self.func.delay = self.delay_text.get()
        self.root.update_func()
        self.root.save_bot()
        self.destroy()
