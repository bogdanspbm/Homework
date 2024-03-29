from BotEngine.Editor import EditorClass
from BotEngine.GUI import App
import datetime as time


def on_closing():
    for thread in app.threads:
        thread.active = False

    root.destroy()
    exit()


if __name__ == '__main__':
    print(time.datetime.now().minute)
    bot_editor = EditorClass.Editor()

    root = App.tk.Tk()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    app = App.Main(root, bot_editor)
    # app.pack()

    root.title('Bot Engine')
    root.iconbitmap('../Sprites/MainIco2.ico')
    root.geometry("1000x500+300+200")
    root.resizable(True, True)
    root.mainloop()
