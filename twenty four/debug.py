# import tkinter as tk
#
# root__ = tk.Tk()
#
# # 创建一个 Canvas 控件
# canvas = tk.Canvas(root__, width=800, height=600)
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # 创建一个 Label 控件
# label = tk.Label(root__, text="Hello, world!")
# label.pack()
#
# # 创建一个 Radiobutton 控件
# radio = tk.Radiobutton(canvas, text="Option 1", variable=tk.IntVar(), value=1)
#
# # 计算 Radiobutton 控件的坐标
# canvas_x = canvas.canvasx(canvas.winfo_rooty())
# canvas_y = canvas.canvasy(canvas.winfo_rooty())
# radio_x = canvas_x + (canvas.winfo_width() - radio.winfo_reqwidth()) / 2
# radio_y = canvas_y + (canvas.winfo_height() - radio.winfo_reqheight()) / 2
#
# # 将 Radiobutton 控件放置在屏幕中央
# canvas.create_window(radio_x, radio_y, anchor=tk.CENTER, window=radio)
#
# # 运行主事件循环
# root.mainloop()
import tkinter as tk

root = tk.Tk()

# 创建一个 Canvas 控件
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建一个 Scrollbar 控件
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 将 Scrollbar 控件绑定到 Canvas 控件上
canvas.configure(yscrollcommand=scrollbar.set)

# 向 Canvas 控件中添加一些示例内容
for i in range(100):
    canvas.create_line(i, 0, i, 50)

# 运行主事件循环
root.mainloop()