import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# 创建一个Canvas控件
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 创建一个Scrollbar控件
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# 创建一个Listbox控件，并将其放置在Canvas中
listbox = tk.Listbox(canvas, width=100)
listbox.pack(side="left")

# 将Listbox添加到Canvas中，并设置滚动条
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=canvas.yview)

# 创建一个Frame控件，用于放置Radiobutton
frame = tk.Frame(canvas, width=200, height=200)

# 创建Radiobutton控件，并将其放置在Frame中
for i in range(10):
    radio_button = tk.Radiobutton(frame, text=f"Font {i}")
    radio_button.place(x=10, y=i*30)

# 将Frame控件放置在Canvas中
canvas.create_window((0, 0), window=frame, anchor="nw")

# 创建一个Canvas控件，用于显示选中的字体
selected_font_canvas = tk.Canvas(root, width=200, height=200, bg="white")
selected_font_canvas.place(x=320, y=0)

# 创建一个Label控件，用于显示当前选中的字体
selected_font_label = tk.Label(selected_font_canvas, text="")
selected_font_label.place(x=10, y=10)

# 创建一个Button控件，用于清除选中的字体
clear_button = tk.Button(selected_font_canvas, text="Clear")
clear_button.place(x=100, y=50)

# 绑定事件处理程序
def select_font(event):
    index = listbox.curselection()
    if index:
        font = listbox.get(index[0])
        selected_font_label.config(text=f"Selected font: {font}")
        selected_font_canvas.delete("all")
        for i in range(10):
            if font == f"Font {i}":
                radio_button = canvas.find_all(".Radiobutton")[i]
                canvas.itemconfig(radio_button, fill="black")
            else:
                radio_button = canvas.find_all(".Radiobutton")[i]
                canvas.itemconfig(radio_button, fill="white")
    selected_font_canvas.update()

# 绑定事件处理程序
canvas.bind("<ButtonRelease-1>", select_font)

root.mainloop()
