import inspect
from tkinter import *

root = Tk()

# class my_listbox(Listbox):
#     def __init__(self, master=None, **kwargs):
#         super().__init__(master, **kwargs)
#     def itemconfig(self, index, **kw):
#         if 'font' in kw:
#             kw["font"] = self.font
#         return super().itemconfigure(index, **kw)
#
#
# listbox = Listbox(root)
# listbox.insert('end', 'hello')
# text = Text(listbox, font=('Arial', 12))
# listbox.itemconfig('end', text)

print(inspect.getsource())
# print(inspect.getsource(Listbox))

# def _configure(self, cmd, cnf, kw):
#     """Internal function."""
#     if kw:
#         cnf = _cnfmerge((cnf, kw))
#     elif cnf:
#         cnf = _cnfmerge(cnf)
#     if cnf is None:
#         return self._getconfigure(_flatten((self._w, cmd)))
#     if isinstance(cnf, str):
#         return self._getconfigure1(_flatten((self._w, cmd, '-' + cnf)))
#     self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
# # These used to be defined in Widget:
#
# def configure(self, cnf=None, **kw):
#     """Configure resources of a widget.
#
#     The values for resources are specified as keyword
#     arguments. To get an overview about
#     the allowed keyword arguments call the method keys.
#     """
#     return self._configure('configure', cnf, kw)
#
def itemconfigure(self, index, cnf=None, **kw):
    """Configure resources of an ITEM.

    The values for resources are specified as keyword arguments.
    To get an overview about the allowed keyword arguments
    call the method without arguments.
    Valid resource names: background, bg, foreground, fg,
    selectbackground, selectforeground."""
    return self._configure(('itemconfigure', index), cnf, kw)


itemconfig = itemconfigure
