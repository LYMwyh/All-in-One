from tkinter import *
from tkinter import ttk

# 创建一个窗口
window = Tk()
window.title("Combobox and Menubutton Example")

# 创建一个Combobox控件
combo_box = ttk.Combobox(window, values=["Option 1", "Option 2", "Option 3"])
combo_box.pack()

# 创建一个Menubutton控件
menu_button = Menubutton(window, text="Menu", indicatoron=False)
menu = Menu(menu_button, tearoff=0)
menu_button["menu"] = menu

menu.add_command(label="Option 1")
menu.add_command(label="Option 2")
menu.add_command(label="Option 3")
menu.add_command(label="Exit", command=window.quit)
menu.add_separator()
menu.add_command(label="Quit", command=window.quit)
menu_button["menu"] = menu
menu_button.place(relx=0, rely=0.9)

window.mainloop()

