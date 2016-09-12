# import csv
# facultyFile = open('faculty.csv')
# facultyReader = csv.reader(facultyFile)
# facultyData = list(facultyReader)

# for rows in facultyData:
# 	index = rows[0]
# 	degree = rows[1]
# 	title = rows[2]
# 	email = rows[3]

# 	mydict = {index: }


# import csv
# with open('faculty.csv') as facultyFile:
# 	dictionary = dict(filter(None, csv.reader(facultyFile)))

# print dictionary
# # 
# # 
# import csv
# reader = csv.reader(open('faculty.csv'))

# faculty_dict = {}
# for row in reader:
# 	key = row[0]
# 	if key in faculty_dict:
# 		pass
# 	faculty_dict[key] = row[1:]
# print faculty_dict


import csv
facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

def differentDegrees(facultyData):
	facultyList = []
	facultyValues = []
	facultyDict = dict()
	count = 0
	counter = 0
	for row in facultyData:
		# Create the index
		if row[0] not in facultyList and count > 0:
			facultyList.append(row[0])
		count += 1
		# print facultyData
	count = 0
	for row in facultyData:
		if row[1:] not in facultyList and count > 0:
			facultyValues.append(row[1:])
		count += 1

	return facultyList, facultyValues


listOfFacultyIndex, listOfFacultyValues = differentDegrees(facultyData)
# print listOfFacultyIndex

a = zip(listOfFacultyIndex, listOfFacultyValues)
# print a
print dict(facultyData)

# print facultyData
