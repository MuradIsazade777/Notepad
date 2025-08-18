import tkinter as tk
from tkinter import filedialog, messagebox

class FileMenu:
    def __init__(self, root, menu_bar, text_area):
        self.root = root
        self.text_area = text_area
        self.file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Saved", "File saved successfully ✅")
