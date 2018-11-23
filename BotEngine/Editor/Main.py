from BotEngine.Editor import EditorClass
from BotEngine.GUI import HUD

if __name__ == '__main__':
    editor = EditorClass.Editor()

    root = HUD.tk.Tk()

    app = HUD.Main(root, editor)
    app.pack()

    root.title('Bot Engine')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()