import tkinter as tk

class MouseClicker(tk.Frame):
    def __init__(self, master):
        super(MouseClicker, self).__init__(master)
        self.button_clicks = 0
        self.labelvariable = tk.IntVar()
        self.createWidgets()

    def createWidgets(self):
        self.labelvariable.set(60)
        self.timeLabel = tk.Label(self, text = "Time:", font = ('Helvetica', 20))
        self.timeLabel.pack(side = tk.TOP)
        self.countdownLabel = tk.Label(self, textvariable = self.labelvariable, font = ('Helvetica', 50))
        self.countdownLabel.pack(side = tk.TOP)
        self.countButton = tk.Button(self, text = "Start", command = self.update_count, bg = "black", fg="white", height = 3, width="11")
        self.countButton.pack(side = tk.TOP)
        self.scoreLabel = tk.Label(self, text = "\n", font = ('Helvetica', 10))
        self.scoreLabel.pack(side = tk.TOP)
        self.authorLabel = tk.Label(self, text = "\nAuthor: Michał Łukowiak", font = ('Helvetica', 7))
        self.authorLabel.pack(side = tk.TOP)

    def update_count(self):
        if self.labelvariable.get() == 60:
            self.manage_countdown()
        if self.labelvariable.get() != 0:
            self.button_clicks += 1
            self.countButton.config(text = "Counter: {}".format(self.button_clicks))
        else:
            self.countButton["state"] = "disabled"
            self.labelvariable.set("Time's up!")
            self.countButton["text"] = "Done!"
            self.scoreLabel["text"] = "\nYou reach " + str(round(int(self.button_clicks)/60,2)) + " clicks per second!"

    def manage_countdown(self):
        if self.labelvariable.get() != 0:
            self.labelvariable.set(self.labelvariable.get() - 1)
            self.after(1000, self.manage_countdown)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Mouse Clicker")
    root.iconbitmap('mc.ico')
    root.geometry("350x250")
    app = MouseClicker(root).pack()
    root.mainloop()