import tkinter as tk

window = tk.Tk()

window.geometry('150x150')

label = tk.Label(
    text="Введите имя",
    height=5
)
entry = tk.Entry()

label.pack()
entry.pack()

window.mainloop()