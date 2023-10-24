import tkinter as tk

def print_text(i=0):
    # 如果所有的文本都已经打印完毕，就返回
    if i >= len(message):
        return
    # 否则，向Text控件中添加下一个字符
    text.insert(tk.END, message[i])
    # 100毫秒后再次调用这个函数
    root.after(100, print_text, i+1)

root = tk.Tk()
text = tk.Text(root)
text.pack()

# 设置Text控件为只读
text.config(state='normal')

message = "Hello, world!"
# 开始打印文本
print_text()

root.mainloop()
