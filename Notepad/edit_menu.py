import tkinter as tk

class EditMenu:
    def __init__(self, root, menu_bar, text_area):
        self.text_area = text_area
        self.edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
