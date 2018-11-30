from BotEngine.Editor import EditorClass
from BotEngine.GUI import App


def on_closing():
    print('here')
    root.destroy()
    exit()
    for thread in app.threads:
        thread.stop()


if __name__ == '__main__':
    bot_editor = EditorClass.Editor()

    root = App.tk.Tk()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    app = App.Main(root, bot_editor)
    app.pack()

    root.title('Bot Engine')
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
