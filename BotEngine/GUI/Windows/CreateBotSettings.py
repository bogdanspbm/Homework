import tkinter as tk
from tkinter import ttk
from BotEngine.GUI.MyWidgets.MyButton import MyButton


class Child(tk.Toplevel):
    def __init__(self, root, bot):
        super().__init__(root)
        self.root = root
        self.bot = bot
        self.button_image = tk.PhotoImage(file='../Sprites/Button_0.png')
        self.button_image_clicked = tk.PhotoImage(file='../Sprites/Button_1.png')
        self.init_child()

    def init_child(self):
        self.title('Create Bot')
        self.geometry('700x400+400+300')
        self.resizable(False, False)

        self.frame = tk.Frame(self)

        self.frame.columnconfigure(0, pad=3)
        self.frame.columnconfigure(1, pad=3)
        self.frame.rowconfigure(0, pad=3)
        self.frame.rowconfigure(1, pad=3)

        label_desc = tk.Label(self.frame, text='Bot Name:')
        label_desc.grid(row=0, column=0, sticky=tk.W)

        self.enter_name = ttk.Entry(self.frame)
        self.enter_name.insert(tk.END, self.bot.Name)
        self.enter_name.grid(row=0, column=1, sticky=tk.W)


        self.enter_button = MyButton(self.frame, image1=self.button_image, image2=self.button_image_clicked, mytext='Enter', mycommand=self.create_bot)
        self.enter_button.grid(row=1, column=0)

        #self.btn_enter = tk.Button(self.frame,borderwidth=0,
        #                           command=self.create_bot, image = self.button_image)
        #self.btn_enter.grid(row=1, column=0, sticky=tk.W)

        self.frame.pack()
        # self.grab_set()
        self.focus_set()

    def button_start_overlap(self, event, button):
        button.configure(image=self.button_image_clicked)

    def button_stop_overlap(self, event, button):
        button.configure(image=self.button_image)

    def create_bot(self):
        self.root.engine.createBot(self.enter_name.get(), 'TOKEN')
        self.root.update_combobox()
        self.destroy()
