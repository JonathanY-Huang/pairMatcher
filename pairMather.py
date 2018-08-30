import os.path
import pickle
import random

if not os.path.exists("students.txt"):
	print("Please add a list of students!")
else:
	studentList = open("students.txt", "r")
	pairs = open("pairs.txt", "w")

	students = []
	for line in studentList:
		students.append(line.rstrip("\n"))

	try:
		prevMatched = pickle.load(open("prevCombinations.p","rb"))
	except:
		prevMatched = {}

	while len(students) > len(students) % 2:
		first = random.choice(students)
		students.remove(first)

		second = ""
		unique = False
		while not unique:
			second = random.choice(students)
			try:
				if prevMatched[first] != second:
					unique = True
			except:
				unique = True
					
		students.remove(second)

		prevMatched[first] = second
		prevMatched[second] = first
		
		pairs.write('{} - {}\n'.format(first, second))

	pairs.write(students[0])

	pickle.dump(prevMatched, open("prevCombinations.p", "wb"))
	

