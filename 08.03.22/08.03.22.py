from tkinter import *

root = Tk()

name = StringVar()

name_label = Label(text="Введите имя:")

name_label.grid(row=0, column=0, sticky="w")

name_entry = Entry(textvariable=name)

name_entry.grid(row=0, column=1, padx=5, pady=5)

root.mainloop()