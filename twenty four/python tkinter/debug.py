import tkinter as tk

root = tk.Tk()

children = tk.Toplevel(root)

print(root.winfo_children())

root.mainloop()
