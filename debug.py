Operators = ['+', '-', '*', '/']
answer = []
complete_answer = ['(', 8.0, '+', 8.0, '-', 13.0, ')', '*', 8.0]

Whole_Answers = []
the_Selected_Operators = []
Four_Numbers = []


def before_or_after_one(index_of_one, before):
	global complete_answer
	if before is True:
		if complete_answer[index_of_one + 1] == '/':
			return False
		elif complete_answer[index_of_one + 1] == '+' or complete_answer[index_of_one + 1] == '-':
			return True
		before = -1
	else:
		if complete_answer[index_of_one - 1] == '+' or complete_answer[index_of_one - 1] == '-':
			return True
		before = 1
	while True:
		index_of_one += before
		if index_of_one < 0 or index_of_one >= len(complete_answer):
			return True
		if type(complete_answer[index_of_one]) is chr:
			if complete_answer[index_of_one] == '(' or complete_answer[index_of_one] == ')':
				return True
			elif complete_answer[index_of_one] == '/' and before == -1:
				return False
			elif complete_answer[index_of_one] == '+' or complete_answer[index_of_one] == '-':
				return True
		elif type(complete_answer[index_of_one]) is float and complete_answer[index_of_one] != 1:
			return False


def simplify_formula_first_part():
	global complete_answer
	layer = 0
	whether_found_addition_or_subtraction = [False]
	whether_found_multiplication_or_division = [False]
	brackets = []
	step = 0
	whether_changed = False
	while True:
		if step == len(complete_answer):
			if whether_changed is False:
				break
			else:
				step = 0
				whether_changed = False
		# brackets.clear()
		symbol = complete_answer[step]
		if symbol == '(':
			layer += 1
			if len(whether_found_multiplication_or_division) == layer:
				whether_found_multiplication_or_division.append(False)
				whether_found_addition_or_subtraction.append(False)
			else:
				whether_found_multiplication_or_division[layer] = False
				whether_found_addition_or_subtraction[layer] = False
			brackets.append(step)
		if symbol == ')':
			decision_front = False
			decision_back = False
			change_symbol_from_subtraction = False
			change_symbol_from_division = False
			if whether_found_multiplication_or_division[layer] and whether_found_addition_or_subtraction[
				layer] is False:
				decision_front = True
				decision_back = True
				if brackets[layer - 1] != 0 and complete_answer[brackets[layer - 1] - 1] == '/':
					change_symbol_from_division = True
			elif brackets[layer - 1] != 0 and complete_answer[brackets[layer - 1] - 1] == '/':
				pass
			else:
				if brackets[layer - 1] != 0:
					if (complete_answer[brackets[layer - 1] - 1] != '*' and complete_answer[
						brackets[layer - 1] - 1] != '/') or (
							complete_answer[brackets[layer - 1] - 2] == 1 and before_or_after_one(
						brackets[layer - 1] - 2, True)):
						decision_front = True
						if complete_answer[brackets[layer - 1] - 1] == '-':
							change_symbol_from_subtraction = True
				else:
					decision_front = True
				if step != len(complete_answer) - 1:
					if (complete_answer[step + 1] != '*' and complete_answer[step + 1] != '/') or (
							complete_answer[step + 2] == 1 and before_or_after_one(step + 2, False)):
						decision_back = True
				else:
					decision_back = True
			if decision_front and decision_back:
				whether_changed = True
				if change_symbol_from_subtraction or change_symbol_from_division:
					temporary_layer = 0
					for temporary_step in range(brackets[layer - 1] + 1, step):
						if change_symbol_from_subtraction and temporary_layer == 0 and complete_answer[
							temporary_step] == '+':
							complete_answer[temporary_step] = '-'
						elif change_symbol_from_subtraction and temporary_layer == 0 and complete_answer[
							temporary_step] == '-':
							complete_answer[temporary_step] = '+'
						elif change_symbol_from_division and temporary_layer == 0 and complete_answer[
							temporary_step] == '*':
							complete_answer[temporary_step] = '/'
						elif change_symbol_from_division and temporary_layer == 0 and complete_answer[
							temporary_step] == '/':
							complete_answer[temporary_step] = '*'
						elif complete_answer[temporary_step] == '(':
							temporary_layer += 1
						elif complete_answer[temporary_step] == ')':
							temporary_layer -= 1
				if whether_found_multiplication_or_division[layer]:
					whether_found_multiplication_or_division[layer - 1] = True
				if whether_found_addition_or_subtraction[layer]:
					whether_found_addition_or_subtraction[layer - 1] = True
				complete_answer.pop(brackets[layer - 1])
				complete_answer.pop(step - 1)
				step -= 2
			brackets.pop()
			layer -= 1
		if symbol == '+' or symbol == '-':
			whether_found_addition_or_subtraction[layer] = True
		elif symbol == '*' or symbol == '/':
			whether_found_multiplication_or_division[layer] = True
		step += 1


def representative_of_the_formula(whole_list):
	if type(whole_list) is list:
		for part_of_list in whole_list:
			if type(part_of_list) is list:
				first_number = representative_of_the_formula(part_of_list)
				if first_number is False:
					continue
				else:
					return first_number
			elif type(part_of_list) is float:
				return part_of_list
		return False
	elif type(whole_list) is float:
		return whole_list
	elif type(whole_list) is chr:
		return False


def simplify_formula_third_part(part_of_group):
	# ['+', 121.0, '/', 11.0, '*', 4.0]
	if len(part_of_group) < 3:
		return part_of_group
	# [39.0, '-', 26.0]
	sort_list = []
	for step in range(len(part_of_group)):
		symbol = part_of_group[step]
		if type(symbol) is not str:
			sort_list.append(
				{"num": representative_of_the_formula(symbol), "operator": part_of_group[step - 1], "index": step})
	min_number = 0
	for step in range(len(sort_list)):
		element = sort_list[step]
		if element["operator"] == '*':
			if sort_list[min_number]["num"] > element["num"]:
				min_number = step
			elif sort_list[min_number]["num"] == element["num"]:
				min_number = step
	if min_number != 0:
		part_of_group[sort_list[0]["index"]], part_of_group[sort_list[min_number]["index"]] = part_of_group[
			sort_list[min_number]["index"]], part_of_group[sort_list[0]["index"]]
		sort_list[min_number]["num"] = sort_list[0]["num"]
	first_number = sort_list[0]["index"] + 1
	del sort_list[0]
	sort_list.sort(reverse=False, key=lambda sort_num: sort_num["num"])
	new_list = [_ for _ in part_of_group[0:first_number]]
	index_of_sort_list = 0
	for step in range(first_number, len(part_of_group), 2):
		index = sort_list[index_of_sort_list]["index"]
		new_list.append(part_of_group[index - 1])
		new_list.append(part_of_group[index])
		index_of_sort_list += 1
	return new_list


def split_list(whole_list):
	if type(whole_list) is list:
		new_list = []
		for part_of_list in whole_list:
			temporary_list = split_list(part_of_list)
			if type(temporary_list) is not list:
				new_list.append(temporary_list)
			else:
				for symbol in temporary_list:
					new_list.append(symbol)
		return new_list
	else:
		return whole_list


def simplify_formula_forth_part(group):
	compare_nums = []
	for step in range(len(group)):
		part_of_group = group[step]
		first_number = representative_of_the_formula(part_of_group)
		compare_nums.append({"num": first_number, "operator": part_of_group[0], "index": step})
	compare_nums.sort(reverse=False, key=lambda sort_num: sort_num["num"])
	for step in range(len(compare_nums)):
		element = compare_nums[step]
		if element["operator"] == '+':
			compare_nums[0], compare_nums[step] = compare_nums[step], compare_nums[0]
			break
	new_group = []
	for element in compare_nums:
		temporary_group = split_list(group[element["index"]])
		for symbol in temporary_group:
			new_group.append(symbol)
	del new_group[0]
	return new_group


def simplify_formula_second_part(first):
	global complete_answer
	group = []
	temporary_group = ['+']
	step = first
	while step < len(complete_answer):
		symbol = complete_answer[step]
		if symbol == '+' or symbol == '-':
			temporary_group = simplify_formula_third_part(temporary_group)
			# print(temporary_group, 1)
			group.append([_ for _ in temporary_group[:]])
			temporary_group.clear()
		
		if symbol == '(':
			temporary_list, step = simplify_formula_second_part(step + 1)
			temporary_list.insert(0, '(')
			temporary_list.append(')')
			temporary_group.append([_ for _ in temporary_list])
			step += 1
			continue
		if symbol == ')':
			break
		temporary_group.append(symbol)
		step += 1
	temporary_group = simplify_formula_third_part(temporary_group)
	# print(temporary_group, 2)
	group.append([_ for _ in temporary_group])
	group = simplify_formula_forth_part(group)
	# print(group, 3)
	return group, step


simplify_formula_first_part()
complete_answer, n = simplify_formula_second_part(0)
print(complete_answer)
