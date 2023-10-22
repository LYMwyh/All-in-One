import tkinter as tk

def validate_input(new_text):
    if not new_text.isdigit() and "." not in new_text:
        return False
    return True

root = tk.Tk()

entry = tk.Entry(root, validate="key", validatecommand=(root.register(validate_input), "%S"))
entry.pack()

root.mainloop()
