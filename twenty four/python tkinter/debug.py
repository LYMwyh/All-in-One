from tkinter import *

root = Tk()

frame1 = Frame(root, bg='black')
frame2 = Frame(root, bg='green')
label = Label(frame1, text='1111')
frame1.pack(side='left')
frame2.pack(side='right')
label.pack()

root.mainloop()
