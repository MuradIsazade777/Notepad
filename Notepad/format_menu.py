import tkinter as tk
from tkinter import colorchooser, font

class FormatMenu:
    def __init__(self, root, menu_bar, text_area):
        self.text_area = text_area
        self.root = root
        self.format_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Format", menu=self.format_menu)

        self.format_menu.add_command(label="Change Font", command=self.change_font)
        self.format_menu.add_command(label="Change Color", command=self.change_color)
        self.format_menu.add_command(label="Toggle Wrap", command=self.toggle_wrap)

    def change_font(self):
        self.text_area.config(font=("Arial", 14, "bold"))

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def toggle_wrap(self):
        current = self.text_area.cget("wrap")
        self.text_area.config(wrap="none" if current == "word" else "word")
