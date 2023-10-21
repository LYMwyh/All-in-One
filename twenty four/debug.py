from tkinter import *


def printout():
	content = text.get('1.0', 'end')
	print(content.split('\n'))


root = Tk()
text = Text(root)
button = Button(root, text="button", command=lambda: printout())
text.place(relx=0, rely=0, relwidth=0.5, relheight=1)
button.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
text.insert('end', '111111')


root.mainloop()
