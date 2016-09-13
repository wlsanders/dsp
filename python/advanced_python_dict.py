

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


#This function finds the last names of the professors
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

#This creates our dictionary for Q6 with a key of last name and value pairs. 
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
# print first3pairs

"""
****

Question 7

****
"""
# print listOfFacultyIndex
# print listOfFacultyValues

def breakingUpName(listOfFacultyIndex):
	newNameList = []
	count = 0
	for name in listOfFacultyIndex:
		delimiter = " "
		split = name.split(delimiter)
		if len(split) == 3 and "." not in split[0]:
			newNameList += [(split[0], split[2])]
		elif len(split) == 2:
			newNameList += [(split[0], split[1])]
		elif "." in split[0]:
			newNameList += [(split[1], split[2])]
	# print newNameList
	return newNameList
	

newNameList = breakingUpName(listOfFacultyIndex) 

def newFacultyDictionary(newNameList, listOfFacultyValues):
	faculty_dict = dict()
	for count in xrange(len(newNameList)):
		# print count
		if newNameList[count] not in faculty_dict:
			faculty_dict[newNameList[count]] = [listOfFacultyValues[count]]
		else:
			faculty_dict[newNameList[count]] += [listOfFacultyValues[count]]
	return faculty_dict
	# print faculty_dict



newFaculty_dict = newFacultyDictionary(newNameList, listOfFacultyValues)
# print newFaculty_dict
first3pairs = {k: newFaculty_dict[k] for k in newFaculty_dict.keys()[:3]}

"""
Q7
"""
sortedDict = sorted(newFaculty_dict.items(), key=lambda newFaculty_dict: newFaculty_dict[1], reverse=True)

print sortedDict


