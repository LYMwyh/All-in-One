from tkinter import *
import algorithm
a = 0

for i in range(1, 14):
	for j in range(1, 14):
		for x in range(1, 14):
			for y in range(1, 14):
				algorithm.Four_Numbers = [i, j, x, y]
				algorithm.calculate_the_whole_answers()
				print(a)
				a += 1