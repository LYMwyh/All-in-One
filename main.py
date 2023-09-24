import random

print("Here is a game:")
print("I will give you 4 integer,you need to use these four integer to calculate 24.")

Operators = ['+', '-', '*', '/']
answer = []


def calculate_the_answer():
	global answer
	step = 0
	layer = 0
	whether_use_addition_and_subtraction = [False]
	whether_use_multiplication_and_division = [True]
	whether_found_multiplication_or_division = [False]
	# while len(answer) != 1:
	for i in range(100):
		# print(answer)
		if step == len(answer):
			step = 0
			whether_use_addition_and_subtraction = [not i for i in whether_found_multiplication_or_division]
			whether_use_multiplication_and_division = [True for _ in whether_use_multiplication_and_division]
			whether_found_multiplication_or_division = [False for _ in whether_found_multiplication_or_division]
		symbol = answer[step]
		if symbol == '(':
			if len(whether_found_multiplication_or_division) - 1 == layer:
				whether_found_multiplication_or_division.append(False)
				whether_use_multiplication_and_division.append(True)
				whether_use_addition_and_subtraction.append(False)
			layer += 1
			step += 1
			continue
		if symbol == ')':
			layer -= 1
			if answer[step - 2] == '(':
				answer.pop(step - 2)
				answer.pop(step - 1)
				step -= 1
			else:
				step += 1
			continue
		if whether_use_addition_and_subtraction[layer]:
			if symbol == '+':
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[step + 1] == ')':
					pass
				else:
					answer[step - 1] += answer[step + 1]
					del answer[step: step + 2]
					continue
			elif symbol == '-':
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[step + 1] == ')':
					pass
				else:
					answer[step - 1] -= answer[step + 1]
					del answer[step: step + 2]
					continue
		if whether_use_multiplication_and_division[layer]:
			if symbol == '*':
				whether_found_multiplication_or_division[layer] = True
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[step + 1] == ')':
					whether_use_multiplication_and_division[-1] = False
				else:
					answer[step - 1] *= answer[step + 1]
					del answer[step: step + 2]
					continue
			elif symbol == '/':
				whether_found_multiplication_or_division[layer] = True
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[step + 1] == ')':
					whether_use_multiplication_and_division[-1] = False
				else:
					if answer[step + 1] == 0:
						answer = [0]
						break
					answer[step - 1] /= answer[step + 1]
					del answer[step: step + 2]
					continue

		step += 1


def calculate_the_whole_answers():
	global answer, Four_Numbers, Operators, the_Selected_Operators, complete_answer
	for first_element in range(0, 4):
		Four_Numbers[0], Four_Numbers[first_element] = Four_Numbers[first_element], Four_Numbers[0]
		for second_element in range(1, 4):
			Four_Numbers[1], Four_Numbers[second_element] = Four_Numbers[second_element], Four_Numbers[1]
			for third_element in range(2, 4):
				Four_Numbers[2], Four_Numbers[third_element] = Four_Numbers[third_element], Four_Numbers[2]
				
				for the_First_Operator in Operators:
					the_Selected_Operators.append(the_First_Operator)
					for the_Second_Operator in Operators:
						the_Selected_Operators.append(the_Second_Operator)
						for the_third_Operator in Operators:
							the_Selected_Operators.append(the_third_Operator)
							for Type_of_Brackets in range(7):
								# a = Four_Numbers[0]
								# b = Four_Numbers[1]
								# c = Four_Numbers[2]
								# d = Four_Numbers[3]
								answer.clear()
								for Create_the_Answer in range(4):
									# 0. (a b) c d
									# 1. a (b c) d
									# 2. a b (c d)
									# 3. (a b c) d
									# 4. a (b c d)
									# 5. (a b)(c d)
									# 6. a b c d
									if Create_the_Answer == 0 and (
											Type_of_Brackets == 0 or Type_of_Brackets == 3 or Type_of_Brackets == 5):
										answer.append("(")
									elif Create_the_Answer == 1 and (
											Type_of_Brackets == 1 or Type_of_Brackets == 4):
										answer.append("(")
									elif Create_the_Answer == 2 and (
											Type_of_Brackets == 2 or Type_of_Brackets == 5):
										answer.append("(")
									
									answer.append(int(Four_Numbers[Create_the_Answer]))
									
									if Create_the_Answer == 1 and (Type_of_Brackets == 0 or Type_of_Brackets == 5):
										answer.append(")")
									elif Create_the_Answer == 2 and (
											Type_of_Brackets == 1 or Type_of_Brackets == 3):
										answer.append(")")
									elif Create_the_Answer == 3 and (
											Type_of_Brackets == 2 or Type_of_Brackets == 4 or Type_of_Brackets == 5):
										answer.append(")")
									
									if Create_the_Answer < 3:  # 0 , 1 , 2
										answer.append(the_Selected_Operators[Create_the_Answer])
								
								complete_answer = [_ for _ in answer]
								# print("".join(list(map(str, complete_answer))))
								calculate_the_answer()
								if answer == [24]:
									if complete_answer not in Whole_Answers:
										Whole_Answers.append(complete_answer)
							
							the_Selected_Operators.pop()
						the_Selected_Operators.pop()
					the_Selected_Operators.pop()


Answer_of_Whether_Play = input("Do you want to play it with me?(YES/NO)")
print("OK!")
while Answer_of_Whether_Play:
	Whole_Answers = []
	the_Selected_Operators = []
	Four_Numbers = [float(random.randint(1, 13)), float(random.randint(1, 13)), float(random.randint(1, 13)), float(random.randint(1, 13))]
	print("Here is four numbers: %d , %d , %d , %d ." % (Four_Numbers[0], Four_Numbers[1], Four_Numbers[2], Four_Numbers[3]))
	print("Did you find the answer(s)?")
	Answer_of_Whether_Want_to_Know_the_Whole_Answers = input("Do you want to know the whole answer(s)?(YES/NO)")
	if Answer_of_Whether_Want_to_Know_the_Whole_Answers == "YES":
		print("OK!")
		calculate_the_whole_answers()
		if len(Whole_Answers) == 0:
			print("There is no any answers!")
		else:
			for Each_Answer in Whole_Answers:
				print(''.join(list(map(str, Each_Answer))) + "=24")
	elif Answer_of_Whether_Want_to_Know_the_Whole_Answers == "NO":
		print("OK!")
	Answer_of_Whether_Play = input("Do you want to play it again?(YES/NO)")
	print("OK!")
	if Answer_of_Whether_Play == "NO":
		break

print("See you next time!")
