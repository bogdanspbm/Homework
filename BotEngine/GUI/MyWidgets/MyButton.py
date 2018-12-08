import tkinter as tk
from tkinter import ttk


class MyButton(tk.Canvas):

    def __init__(self, root=None, image1=None, image2=None, mytext=None,
                 mycommand=None, textsize='15', mybg='#ffffff'):
        self.x = image1.width()
        self.y = image1.height()
        self.textsize = textsize
        super().__init__(root, width=self.x, height=self.y, bd=0,
                         highlightthickness=0, bg=mybg)
        # self.root = root

        # self.width = self.x/2
        # self.height = self.y/2

        # self.configure(scrollregion=(-10000,-10000,10000,10000))
        self.image1 = image1
        self.image2 = image2
        self.text = mytext
        self.mycommand = mycommand
        self.button = None

        self.init_button()

    def init_button(self):

        if self.image1 != None:
            self.myimg = self.create_image(self.x / 2, self.y / 2,
                                           image=self.image1)
            # self.configure(image=self.image1)

        self.bind('<Button-1>', self.click_event)
        self.bind('<Enter>', self.button_start_overlap)
        self.bind('<Leave>', self.button_end_overlap)

        if self.text != None:
            self.new_text = self.create_text(self.x / 2, self.y / 2,
                                             text=self.text,
                                             font=('Roboto', self.textsize))
            # self.new_text = ttk.Label(self, text=self.text)
            # self.new_text.pack()
            pass

    def click_event(self, event):

        if self.mycommand != None:
            self.mycommand()
            pass

    def button_start_overlap(self, event):

        if self.image2 != None:
            self.itemconfigure(self.myimg, image=self.image2)
            # self.configure(image=self.image2)

    def button_end_overlap(self, event):

        if self.image1 != None:
            # self.configure(image=self.image1)
            self.itemconfigure(self.myimg, image=self.image1)
