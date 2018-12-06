import tkinter as tk
from tkinter import ttk


class MyBotButton(tk.Canvas):

    def __init__(self, root=None, image1=None, image2=None, mytext=None,
                 mycommand=None, textsize = '15', mybg = '#ffffff', main_window = -1):
        self.x = image1.width()
        self.y = image1.height()
        self.textsize = textsize
        super().__init__(root, width = self.x, height = self.y, bd=0, highlightthickness=0, bg=mybg)

        if mytext == main_window.last_bot_name:
            main_window.last_bot_button = self

        self.image1 = image1
        self.image2 = image2
        self.text = mytext
        self.mycommand = mycommand
        self.button = None
        self.main_window = main_window

        self.init_button()

    def init_button(self):


            if self.image1 != None and self.text != self.main_window.cur_bot_name:
                self.myimg = self.create_image(self.x/2,self.y/2,image=self.image1)

            if self.image2 != None and self.text == self.main_window.cur_bot_name:
                self.main_window.last_bot_button = self
                self.myimg = self.create_image(self.x / 2, self.y / 2, image=self.image2)

            self.bind('<Button-1>', self.click_event)

            if self.text != None:
                self.new_text = self.create_text(self.x/2,self.y/2,text=self.text,font=('Roboto',self.textsize))


    def click_event(self, event):

        self.main_window.cur_bot_name = self.text
        self.main_window.last_bot_name = self.text

        self.itemconfigure(self.myimg, image=self.image2)

        if self.main_window.last_bot_button != None:
            self.main_window.last_bot_button.itemconfigure(self.main_window.last_bot_button.myimg, image=self.image1)

        self.main_window.last_bot_button = self

        if self.mycommand != None:
            self.mycommand()
            print('here')


