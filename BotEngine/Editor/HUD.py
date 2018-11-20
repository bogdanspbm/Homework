import tkinter as tk
from tkinter import ttk
import os




class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#aaaaaa', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='../Sprites/Button_Test.png')
        button_open_dialog = tk.Button(toolbar,
                                       command=self.open_dialog, bd=0,
                                       compound=tk.TOP, image=self.add_img)

        button_open_dialog.pack(side=tk.LEFT)


        self.combobox = ttk.Combobox(self, values=os.listdir('../Bots'))
        self.combobox.current(0)
        self.combobox.pack()


        self.tree = ttk.Treeview(self, column=('ID', 'description', 'type'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)

        self.tree.column('description', width=30, anchor=tk.CENTER)

        self.tree.column('type', width=30, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')

        self.tree.heading('description', text='Description')

        self.tree.heading('type', text='Type')

        self.tree.pack()


    def open_dialog(self):
        Child()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Create Bot')
        self.geometry('400x200+400+300')
        self.resizable(False, False)

        label_desc = tk.Label(self, text='Enter bot Name')
        label_desc.place(x=50, y=50)

        self.enter_name = ttk.Entry(self)
        self.enter_name.place(x=200, y=50)

        self.accept_img = tk.PhotoImage(file='../Sprites/Button_accept.png')

        btn_enter = ttk.Button(self, image=self.accept_img)
        btn_enter.place(x=100,y=80)
        btn_enter.bind('<btn-1>')

        self.grab_set()
        self.focus_set()





if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Bot Engine')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()