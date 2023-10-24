import tkinter as tk
import platform

root = tk.Tk()

# 创建一个Canvas组件和一个Scrollbar组件
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

# 创建一个Frame组件，并将其添加到Canvas组件中
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# 更新滚动区域并将Scrollbar组件的command属性设置为Canvas组件的yview方法
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)

frame.bind('<Configure>', update_scrollregion)

# 添加一些内容到Frame组件中
for i in range(50):
    tk.Label(frame, text="This is line %i" % i).pack()

# 布局管理
canvas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# 绑定鼠标滚轮事件
def on_mousewheel(event):
    if platform.system() == 'Windows':
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    elif platform.system() == 'Darwin':
        canvas.yview_scroll(int(-1*(event.delta)), "units")
    else:
        if event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")

if platform.system() == 'Windows':
    canvas.bind_all("<MouseWheel>", on_mousewheel)
elif platform.system() == 'Darwin':
    canvas.bind_all("<MouseWheel>", on_mousewheel)
else:
    canvas.bind_all("<Button-4>", on_mousewheel)
    canvas.bind_all("<Button-5>", on_mousewheel)

root.mainloop()

# Ask:
# 这个程序是否能够在手机和平板上运行同样起到鼠标控制滚动的功能

# Answer:
# Python的Tkinter库主要是为桌面环境设计的，它可能无法在手机或平板等触摸屏设备上正常工作。在触摸屏设备上，用户的交互方式（例如滑动和点击）与鼠标和键盘有所不同，因此可能需要使用不同的库或框架来处理这些交互。
#
# 如果你希望在手机或平板上运行Python程序，你可能需要考虑使用如Kivy这样的库，它支持多点触控、手势识别等功能，并且可以在Android、iOS等多种平台上运行。
#
# 请注意，将Python程序部署到手机或平板通常需要一些额外的步骤，例如打包应用、处理权限问题等。你可能需要参考相关的文档和教程来了解更多信息。希望这个信息对你有所帮助！
