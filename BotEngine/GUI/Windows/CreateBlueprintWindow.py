import tkinter as tk
from tkinter import ttk


class Child(tk.Toplevel):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.enter_name = -1
        self.btn_enter = -1
        self.image = tk.PhotoImage(file='../Sprites/Popup_BP.png')
        self.image_bl = tk.PhotoImage(file='../Sprites/ButtonL_0.png')
        self.image_br = tk.PhotoImage(file='../Sprites/ButtonR_0.png')
        self.image_bl_1 = tk.PhotoImage(file='../Sprites/ButtonL.png')
        self.image_br_1 = tk.PhotoImage(file='../Sprites/ButtonR.png')
        self.btn_enter = -1
        self.init_child()

    def init_child(self):
        self.title('Create BP')
        self.geometry('400x200+400+300')
        self.iconbitmap('../Sprites/MainIco.ico')
        self.resizable(False, False)
        self.window = tk.Canvas(self, width=self.image.width(),
                                height=self.image.height(), bd=0,
                                highlightthickness=0)
        self.window.pack(expand=True)
        self.window.create_image(self.image.width() / 2,
                                 self.image.height() / 2,
                                 image=self.image)
        self.img1 = self.window.create_image(303, 180,
                                             image=self.image_bl,
                                             tag='accept')
        self.img2 = self.window.create_image(365, 180,
                                             image=self.image_br,
                                             tag='back')
        self.window.tag_bind('accept', '<Button-1>', self.create_bp)
        self.window.tag_bind('back', '<Button-1>', self.back)

        self.enter_name = tk.Entry(self.window, bg='#e7e7e7', bd=0,
                                   highlightthickness=0, width=15)
        self.enter_name.place(x=218, y=35)

        # self.grab_set()
        self.focus_set()

    def back(self, event=''):
        self.destroy()

    def create_bp(self):
        self.root.engine.CurrentBot.addBlueprint(self.enter_name.get(),
                                                 self.root.engine)
        self.root.update_bp()
        self.destroy()
