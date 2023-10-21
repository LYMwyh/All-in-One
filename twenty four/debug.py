import tkinter as tk
import tkinter.font as font

root = tk.Tk()

# 创建一个字体列表
fonts = ["Helvetica", "Arial", "Times New Roman", "Courier New"]

# 创建一个变量对象，并将其赋值为一个空字符串
var = tk.StringVar(value="")

# 创建一个 radiobutton 控件列表
font_buttons = []
for font_name in fonts:
    font_button = tk.Radiobutton(root, text=font_name, variable=var, value=font_name)
    font_button.pack()
    font_buttons.append(font_button)

# 创建一个 Label 控件，用于显示当前选中的字体
font_label = tk.Label(root, textvariable=var)
font_label.pack()

# 定义回调函数，用于更新 Label 控件的文本
def update_font():
    font_label.config(text=var.get())

# 绑定回调函数，使得当用户点击 radiobutton 控件时，能够更新 Label 控件的文本
for font_button in font_buttons:
    font_button.config(command=update_font)

root.mainloop()
