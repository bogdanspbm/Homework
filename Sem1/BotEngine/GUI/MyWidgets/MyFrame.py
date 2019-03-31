import tkinter as tk
from tkinter import ttk


class MyFrame(tk.Canvas):

    def __init__(self, root=None, image1=None):
        self.x = image1.width()
        self.y = image1.height()

        super().__init__(root, width=self.x, height=self.y)

        self.image1 = image1

        self.init_button()

    def init_button(self):
        if self.image1 != None:
            self.myimg = self.create_image(self.x / 2, self.y / 2,
                                           image=self.image1)
            # self.configure(image=self.image1)
