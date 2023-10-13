from tkinter import *

root = Tk()
size = 10
text = Text(root, font=size)
text.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def ab():
	global size
	size += 1
	text.configure(font=size)
	root.update()


frame = Frame()
button = Button(root, text="1", command=ab)
button.place(relx=0, rely=1, relwidth=1, relheight=0.5)

root.mainloop()
