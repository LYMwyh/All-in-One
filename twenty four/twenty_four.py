import tkinter.font
from tkinter import *
import random
import time
import algorithm
import platform

root = Tk()
root.title("Twenty Four")
root.geometry("800x400+100+100")

Start = Button(root, text="Start")

setting = Button(root, text="Setting")

print_frame_border = Frame(root, bg="white", bd=1)
print_text = Text(print_frame_border, bg="black", fg="white")

input_frame_border = Frame(root, bg="white", bd=1)
input_frame = Frame(input_frame_border, bg="black")
example = Text(input_frame, bg="black", fg="white")
input_text = Text(input_frame, bg="black", fg="white")

button_next = Button(input_frame, text="Next")
button_yes = Button(input_frame, text="YES")
button_no = Button(input_frame, text="NO")
button_close = Button(input_frame, text="closed", command=root.quit)

setting_content = [setting,
                   'setting_window',
                   print_text,
                   button_yes,
                   button_no,
                   example,
                   input_text,
                   button_next,
                   button_close]

setting_content_detail = {
	setting: "Setting",
	'setting_window': 'setting_window',
	print_text: "Print Text",
	button_yes: "Button Yes",
	button_no: "Button No",
	example: "Example",
	input_text: "Input text",
	button_next: "Button Next",
	button_close: "Button Close"
}

fonts = tkinter.font.families()

font_family = {}
for content_name in setting_content:
	font_family[content_name] = tkinter.font.Font(family=fonts[0], size=13)
	if type(content_name) != str:
		content_name.configure(font=font_family[content_name])


def open_setting_window():
	global font_family, setting_content_detail, setting_content
	setting_window = Toplevel(root)
	
	setting_window_canvas = Canvas(setting_window)
	setting_window_canvas_scrollbar = Scrollbar(setting_window, orient="vertical", command=setting_window_canvas.yview)
	setting_window_canvas.pack(side='left', fill='both', expand=True)
	setting_window_canvas_scrollbar.pack(side='right', fill='y')
	
	setting_window_frame = Frame(setting_window_canvas)
	
	setting_window_canvas.create_window((0, 0), window=setting_window_frame, anchor='nw')
	
	def update_scroll_region_and_canvas_size(event):
		setting_window_canvas.configure(scrollregion=setting_window_canvas.bbox('all'))
		setting_window_canvas.configure(yscrollcommand=setting_window_canvas_scrollbar.set)
		setting_window_canvas.configure(width=setting_window_frame.winfo_width(), height=setting_window_frame.winfo_height())
	
	setting_window_canvas.bind('<Configure>', update_scroll_region_and_canvas_size)
	
	def on_mousewheel(event):
		if platform.system() == 'Windows':
			setting_window_canvas.yview_scroll(int(-1*event.delta/120), 'units')
		elif platform.system() == 'Darwin':
			setting_window_canvas.yview_scroll(int(-1*event.delta), 'units')
		else:
			if event.num == 4:
				setting_window_canvas.yview_scroll(-1, 'units')
			elif event.num == 5:
				setting_window_canvas.yview_scroll(1, 'units')
	
	if platform.system() == 'Windows' or platform.system() == 'Darwin':
		setting_window_canvas.bind_all("<MouseWheel>", on_mousewheel)
	else:
		setting_window_canvas.bind_all("<Button-4", on_mousewheel)
		setting_window_canvas.bind_all("<Button-5>", on_mousewheel)
	
	setting_frame = {}
	for content_name in setting_content:
		setting_frame[content_name] = Frame(setting_window_frame)
	
	setting_menu_button = {}
	font_style_vars = []
	for content_name in setting_content:
		font_style_vars.append(StringVar(setting_frame[content_name]))
		font_style_vars[-1].set(font_family[content_name]['family'])
		setting_menu_button[content_name] = Menubutton(setting_frame[content_name],
		                                            font=(font_family[content_name]['family'], 13),
		                                            textvariable=font_style_vars[-1])
	
	def update_font_print(widget, **kwargs):
		if 'font_style' in kwargs:
			font_style = kwargs['font_style']
			font_family[widget]['family'] = font_style
			setting_menu_button[widget].configure(text=font_style, font=(font_style, 13))
		if 'font_size' in kwargs:
			font_size = setting_entry[widget].get()
			if font_size != "":
				font_family[widget]['size'] = int(font_size)
		if 'add_size' in kwargs:
			font_family[widget]['size'] += 1
			setting_entry[widget].delete(0, 'end')
			setting_entry[widget].insert('end', str(font_family[widget]['size']))
		if 'subtract_size' in kwargs:
			font_family[widget]['size'] -= 1
			setting_entry[widget].delete(0, 'end')
			setting_entry[widget].insert('end', str(font_family[widget]['size']))
		
		if widget['state'] == DISABLED:
			widget.configure(state=NORMAL)
			widget.configure(font=font_family[widget])
			widget.configure(state=DISABLED)
		else:
			widget.configure(font=font_family[widget])
	
	setting_menu = {}
	for i, (key_value, element) in enumerate(setting_menu_button.items()):
		setting_menu[key_value] = Menu(element, tearoff=0)
		setting_menu_button[key_value].configure(menu=setting_menu[key_value])
		if key_value == "setting_window":
			continue
		for each_font in fonts:
			setting_menu[key_value].add_radiobutton(label=each_font, font=(each_font, 13), variable=font_style_vars[int(i)],
			                                        command=lambda widget=key_value,
			                                                       new_font=each_font: update_font_print(widget,
			                                                                                             font_style=new_font))
	
	def on_focus_out(entry, widget):
		entry.delete(0, 'end')
		entry.insert('end', str(font_family[widget]['size']))
	
	def only_int_input(P):
		if P.isdigit():
			return True
		elif P == "":
			return True
		else:
			return False
	
	setting_entry = {}
	setting_entry_button = {}
	for content_name in setting_content:
		setting_entry[content_name] = Entry(setting_frame[content_name], validate="key",
		                                 validatecommand=(setting_window_frame.register(only_int_input), '%P'))
		setting_entry[content_name].insert('end', str(font_family[content_name]['size']))
		setting_entry[content_name].bind('<FocusOut>',
		                              lambda event, entry=setting_entry[content_name], widget=content_name: on_focus_out(
			                              entry, widget))
		setting_entry_button[content_name] = Button(setting_frame[content_name], text="Confirm")
		setting_entry_button[content_name].config(
			command=lambda widget=content_name, new_size=True: update_font_print(widget, font_size=new_size))
	
	setting_font_size_frame = {}
	setting_font_size_button = {}
	# icon_up = PhotoImage(file="icon-up.png")
	# icon_down = PhotoImage(file="icon-down.png")
	for content_name in setting_content:
		if content_name == 'setting_window':
			continue
		setting_font_size_frame[content_name] = Frame(setting_frame[content_name])
		setting_font_size_button[content_name] = []
		setting_font_size_button[content_name].append(Button(setting_font_size_frame[content_name], text='up', command=lambda widget=content_name: update_font_print(widget, add_size=True)))
		setting_font_size_button[content_name].append(Button(setting_font_size_frame[content_name], text='down', command=lambda widget=content_name: update_font_print(widget, subtract_size=True)))
	
	setting_widget_hint = {}
	for key, element in setting_content_detail.items():
		setting_widget_hint[key] = []
		if key == 'setting_window':
			continue
		setting_widget_hint[key].append(
			Label(setting_frame[key], text=element, font=font_family['setting_window']))
		setting_widget_hint[key].append(
			Label(setting_frame[key], text=element + ' font style: ', font=font_family['setting_window']))
		setting_widget_hint[key].append(
			Label(setting_frame[key], text=element + ' size: ', font=font_family['setting_window']))
	
	def update_font_in_setting_window(**kwargs):
		global font_family
		if 'update_font_style' in kwargs:
			font_style = kwargs['update_font_style']
			font_family['setting_window']['family'] = font_style
			setting_menu_button['setting_window'].configure(text=font_style, font=(font_style, 13))
		if 'add_size' in kwargs and kwargs['add_size']:
			font_family['setting_window']['size'] += 1
		if 'subtract_size' in kwargs and kwargs['subtract_size']:
			font_family['setting_window']['size'] -= 1
		
		size_add.configure(font=font_family['setting_window'])
		size_subtract.configure(font=font_family['setting_window'])
		for ordinal_number in range(9):
			if ordinal_number == 1:
				continue
			setting_widget_hint[setting_content[ordinal_number]][0].config(font=font_family['setting_window'])
			setting_widget_hint[setting_content[ordinal_number]][1].config(font=font_family['setting_window'])
			setting_widget_hint[setting_content[ordinal_number]][2].config(font=font_family['setting_window'])
	
	# 开始放置
	for each_font in fonts:
		setting_menu['setting_window'].add_radiobutton(label=each_font, font=(each_font, 13),
		                                               variable=font_style_vars[1],
		                                               command=lambda new_font=each_font: update_font_in_setting_window(
			                                               update_font_style=new_font))
	
	setting_menu_button['setting_window'].pack(fill='x', side='top', expand=True)
	
	size_add = Button(setting_frame['setting_window'], text="font size +",
	                  command=lambda: update_font_in_setting_window(add_size=True))
	size_add.configure(font=font_family['setting_window'])
	size_subtract = Button(setting_frame['setting_window'], text="font size -",
	                       command=lambda: update_font_in_setting_window(subtract_size=True))
	size_subtract.configure(font=font_family['setting_window'])
	
	size_add.pack(fill='x', side='left', expand=True)
	size_subtract.pack(fill='x', side='right', anchor="center", expand=True)
	setting_frame['setting_window'].pack(fill='x')
	
	def draw_line(canvas):
		canvas.delete('all')
		canvas.create_line(0, 0, canvas.winfo_width(), 0, width=canvas.winfo_height(), fill='black')
	
	dividing_line = []
	for ordinal_number in range(10):
		if ordinal_number == 1:
			continue
		dividing_line.append(Canvas(setting_window_frame, height=1))
		dividing_line[-1].pack(fill='x')
		dividing_line[-1].bind("<Configure>", lambda event, canvas=dividing_line[-1]: draw_line(canvas))
		if ordinal_number == 9:
			break
		setting_widget_hint[setting_content[ordinal_number]][0].grid(row=0, column=0)
		setting_widget_hint[setting_content[ordinal_number]][1].grid(row=1, column=0)
		setting_menu_button[setting_content[ordinal_number]].grid(row=1, column=1)
		setting_widget_hint[setting_content[ordinal_number]][2].grid(row=2, column=0)
		setting_entry[setting_content[ordinal_number]].grid(row=2, column=1)
		
		setting_font_size_button[setting_content[ordinal_number]][0].pack(side='top', fill='x', expand=True)
		setting_font_size_button[setting_content[ordinal_number]][1].pack(side='bottom', fill='x', expand=True)
		setting_font_size_frame[setting_content[ordinal_number]].grid(row=2, column=2)
		
		setting_entry_button[setting_content[ordinal_number]].grid(row=2, column=3)
		setting_frame[setting_content[ordinal_number]].pack(anchor='center')
	close = Button(setting_window_frame, text="Closed", font=font_family['setting_window'], command=setting_window.destroy)
	close.pack(anchor='center')


setting.configure(command=lambda: open_setting_window())


def printer(content, text=print_text):
	for char in content:
		text.configure(state=NORMAL)
		text.insert('end', char)
		text.configure(state=DISABLED)
		root.update()
		time.sleep(0)
	text.configure(state=NORMAL)
	text.insert('end', '\n')
	text.configure(state=DISABLED)


def whether_know_whole_answer():
	example.place_forget()
	input_text.place_forget()
	button_next.place_forget()
	
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	
	printer("Do you want to know the all the answers?")
	
	button_yes.configure(command=lambda: whole_answers(True))
	button_no.configure(command=lambda: whole_answers(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def submit_answers():
	submit.configure(state=DISABLED)
	input_text.configure(state=DISABLED)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	answers = input_text.get('1.0', 'end')
	answers = answers.split('\n')
	answers.pop()
	# print(Whole_Answers)
	for answer_in_str in answers:
		num = False
		answer = []
		if len(answer_in_str) == 0:
			continue
		for char in answer_in_str:
			try:
				temporary_num = int(char)
				if num:
					answer[-1] *= 10
					answer[-1] += temporary_num
				else:
					num = True
					answer.append(temporary_num)
			except ValueError:
				num = False
				answer.append(char)
		for step in range(len(answer)):
			if type(answer[step]) is int:
				answer[step] = float(answer[step])
		algorithm.simplify_formula_first_part(answer)
		answer, temporary_num = algorithm.simplify_formula_second_part(0, answer)
		for step in range(len(answer)):
			if type(answer[step]) is float:
				answer[step] = int(answer[step])
		answer = ''.join(list(map(str, answer)))
		# print(answer)
		if answer in algorithm.Whole_Answers:
			printer("True")
		else:
			printer("False")
	
	if answers == ['']:
		printer("You did not input any answers!")
	submit.place_forget()
	button_next.configure(command=lambda: whether_know_whole_answer())
	button_next.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


submit = Button(input_frame, text="Submit", command=lambda: submit_answers())


def check_answer(yes):
	button_yes.place_forget()
	button_no.place_forget()
	
	printer("OK!")
	time.sleep(1.0)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	if yes is True:
		printer(
			"Four numbers: %d , %d , %d , %d ." % (
				algorithm.Four_Numbers[0], algorithm.Four_Numbers[1], algorithm.Four_Numbers[2],
				algorithm.Four_Numbers[3]))
		printer("Please input your answer(s) in the input frame.")
		printer("Each line write one answer.You don't need to write '=24' in the end of each line.")
		
		example.configure(state=DISABLED)
		example.place(relx=0, rely=0, relwidth=1, relheight=0.1)
		input_text.configure(state=NORMAL)
		input_text.delete('1.0', 'end')
		input_text.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
		submit.configure(state=NORMAL)
		submit.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
		printer("Example: a+b+c+d", example)
	else:
		whether_know_whole_answer()


def whole_answers(yes):
	button_yes.place_forget()
	button_no.place_forget()
	
	printer('\n')
	printer("OK!")
	time.sleep(1.0)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	if yes is True:
		if len(algorithm.Whole_Answers) == 0:
			printer("There is no any answers!")
		else:
			for Each_Answer in algorithm.Whole_Answers:
				printer(Each_Answer + "=24")
	printer("Do you want to play it again?")
	
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def clicked_yes():
	button_yes.place_forget()
	button_no.place_forget()
	
	algorithm.Whole_Answers = []
	algorithm.the_Selected_Operators = []
	algorithm.Four_Numbers = []
	for _ in range(4):
		algorithm.Four_Numbers.append(float(random.randint(1, 13)))
	
	printer('\n')
	printer('OK!')
	time.sleep(0.2)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	printer("Here is four numbers: %d , %d , %d , %d ." % (
		algorithm.Four_Numbers[0], algorithm.Four_Numbers[1], algorithm.Four_Numbers[2], algorithm.Four_Numbers[3]))
	time.sleep(1)
	
	algorithm.calculate_the_whole_answers()
	
	printer("Did you find any answers?")
	printer("If yes, do you want to check your answer(s)?")
	
	button_yes.configure(command=lambda: check_answer(True))
	button_no.configure(command=lambda: check_answer(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def clicked_no():
	button_yes.place_forget()
	button_no.place_forget()
	
	printer('\n')
	printer("OK!")
	printer("See you next time!")
	
	button_close.place(relx=0, rely=0, relwidth=1, relheight=1)


def start():
	Start.place_forget()
	print_frame_border.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.9)
	print_text.configure(state=DISABLED)
	print_text.place(relx=0, rely=0, relwidth=1, relheight=1)
	input_frame_border.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
	input_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
	setting.place(relx=0, rely=0, relwidth=1, relheight=0.1)
	printer("Here is a game:")
	printer("There will have four random integers from 1 to 13, you need to use these four integers calculate 24.")
	printer("Each integer must and can only be used once.")
	printer("Sometimes, there is no solutions for figuring out 24.")
	printer("\n")
	
	printer("Do you want to play it with me?")
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


Start.configure(command=lambda: start())
Start.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
