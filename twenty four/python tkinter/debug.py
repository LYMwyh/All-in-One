import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text='1111')

button = tk.Button(root, text='111', command=lambda: label.pack())
button.pack()

root.mainloop()
