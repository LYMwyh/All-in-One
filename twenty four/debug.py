import tkinter as tk

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
canvas = tk.Canvas(root)
frame = tk.Frame(canvas)

# 添加滚动条到canvas
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# 添加frame到canvas
canvas.create_window((0,0), window=frame, anchor="nw")

for i in range(50):
    tk.Label(frame, text="This is line %i" % i).pack()

frame.bind("<Configure>", lambda event, Canvas=canvas: onFrameConfigure(Canvas))

root.mainloop()
