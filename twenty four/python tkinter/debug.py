import tkinter as tk



def toggle_state():
    if state.get() == 'normal':
        state.set('disabled')
    else:
        state.set('normal')

root = tk.Tk()


def open_window():
	window = tk.Toplevel(root)
	button2 = tk.Button(window, text='111')
	button2.pack()
	
	def update_button(*args):
		print(args)
		if state.get() == 'normal':
			button2.config(state='normal')
		else:
			button2.config(state='disabled')
	
	state.trace('w', update_button)
	
state = tk.StringVar()
state.set('')


button = tk.Button(root, text="Toggle", command=open_window)
button.pack()

button3 = tk.Button(root, text='112', command=toggle_state)
button3.pack()

root.mainloop()
