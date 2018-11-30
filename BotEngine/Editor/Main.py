from BotEngine.Editor import EditorClass
from BotEngine.GUI import App

if __name__ == '__main__':
    bot_editor = EditorClass.Editor()

    root = App.tk.Tk()

    app = App.Main(root, bot_editor)
    app.pack()

    root.title('Bot Engine')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
