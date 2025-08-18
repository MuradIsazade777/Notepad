import tkinter as tk
from tkinter import messagebox

class HelpMenu:
    def __init__(self, root, menu_bar):
        self.help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.help_menu.add_command(label="About", command=self.about)

    def about(self):
        messagebox.showinfo("About", "Notepad made with Python Tkinter ✨\nBy Murad 😉")
