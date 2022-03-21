import tkinter as tk

class MyButton(tk.Button):
    def __init__(self, text):
        super().__init__(text)
        self.text = "Мой класс - MyButton"
