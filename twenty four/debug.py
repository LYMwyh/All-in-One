import tkinter as tk


root = tk.Tk()

def on_hover(event):
    # 使第二个Label对象闪烁
    label2.config(bg='red', fg='white', borderwidth=5)
    # 设置一个定时器，使第二个Label对象在一定时间后停止闪烁
    label2.after(500, lambda: label2.config(bg='white', fg='black', borderwidth=0))

# 创建两个Label对象
label1 = tk.Label(root, text='Hover over me!')
label2 = tk.Label(root, text='Hello, world!')

# 将鼠标进入事件绑定到第一个Label对象上
label1.bind('<Enter>', on_hover)
label1.pack()

# 将第二个Label对象放置在第一个Label对象下面
label2.pack()

# 进入主事件循环
root.mainloop()
