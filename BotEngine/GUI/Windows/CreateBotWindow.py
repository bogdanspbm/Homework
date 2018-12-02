import tkinter as tk
from tkinter import ttk


class Child(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.enter_name = -1
        self.image = tk.PhotoImage(file='../Sprites/Popup.png')
        self.image_bl = tk.PhotoImage(file='../Sprites/ButtonL_0.png')
        self.image_br = tk.PhotoImage(file='../Sprites/ButtonR_0.png')
        self.image_bl_1 = tk.PhotoImage(file='../Sprites/ButtonL.png')
        self.image_br_1 = tk.PhotoImage(file='../Sprites/ButtonR.png')
        self.btn_enter = -1
        self.init_child()

    def init_child(self):
        self.title('Create Bot')
        self.geometry('400x200+400+300')
        self.resizable(False, False)
        self.window = tk.Canvas(self,width=self.image.width(), height=self.image.height(),bd=0, highlightthickness=0)
        self.window.pack(expand=True)
        self.window.create_image(self.image.width()/2,self.image.height()/2,image=self.image)
        self.window.create_image(100, 180, image=self.image_bl, tag='accept')
        self.window.create_image(300, 180, image=self.image_br, tag='back')

        self.enter_name = ttk.Entry(self.window,width=2)
        self.enter_name.place(x=100,y=50)


        # self.grab_set()
        self.focus_set()

    def create_bot(self):
        self.root.engine.createBot(self.enter_name.get(), 'TOKEN')
        self.root.update_combobox()
        self.destroy()
