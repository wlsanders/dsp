

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



def findingLastName(listOfFacultyValues):
	lastName = []
	for name in listOfFacultyIndex:
		delimiter = " "
		s = name.split(delimiter)
		# print s
		if len(s) == 3:
			lastName.append(s[2])
		elif len(s) == 2:
			lastName.append(s[1])
	return lastName

lastName = findingLastName(listOfFacultyValues)
# faculty_dict[lastName[0]] = listOfFacultyValues[0]
# faculty_dict[lastName[14]] = listOfFacultyValues[14]
# faculty_dict[lastName[15]] = [listOfFacultyValues[15]]
# faculty_dict[lastName[16]] += [listOfFacultyValues[16]]
# faculty_dict[lastName[17]] += [listOfFacultyValues[17]]
# print faculty_dict

def facultyDictionary(lastName, listOfFacultyValues):
	faculty_dict = dict()
	for count in xrange(len(lastName)):
		if lastName[count] not in faculty_dict:
			faculty_dict[lastName[count]] = [listOfFacultyValues[count]]
		else:
			faculty_dict[lastName[count]] += [listOfFacultyValues[count]]
	return faculty_dict
	# print faculty_dict

faculty_dict = facultyDictionary(lastName, listOfFacultyValues)


# print faculty_dict

first3pairs = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}
print first3pairs





