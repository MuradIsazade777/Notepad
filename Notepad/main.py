import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, font

from file_menu import FileMenu
from edit_menu import EditMenu
from format_menu import FormatMenu
from help_menu import HelpMenu


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Notepad")
        self.root.geometry("800x600")

        # Text area
        self.text_area = tk.Text(self.root, wrap="word", font=("Consolas", 14))
        self.text_area.pack(expand=1, fill="both")

        # Scrollbar
        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

        # Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Sub Menus
        FileMenu(self.root, self.menu_bar, self.text_area)
        EditMenu(self.root, self.menu_bar, self.text_area)
        FormatMenu(self.root, self.menu_bar, self.text_area)
        HelpMenu(self.root, self.menu_bar)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
