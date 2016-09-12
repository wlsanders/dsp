

# Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etcimport csv
# 
import csv
facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

def differentDegrees(facultyData):
	degreeType = []
	count = 0
	for row in facultyData:
		# print row
		if row[1] not in degreeType and count > 0:
			degreeType.append(row[1])
		count += 1
	return degreeType


degreeTypes = differentDegrees(facultyData)

# print degreeTypes
def cleaningDegreeTypes(degreeTypes):
	degreeList = dict()
	# print degreeTypes
	for degree in degreeTypes:
		a = degree.replace('.', "")
		if " " not in a:
			if a not in degreeList:
				degreeList[a] = 1
			else:
				degreeList[a] += 1
			# print degreeList, "list"
		else: 
			delimiter = ' '
			b = a.split(delimiter)
			for degree in b:
				if degree not in degreeList:
					degreeList[degree] = 1
				else:
					degreeList[degree] += 1
	return degreeList

cleaningDegreeTypes(degreeTypes)

"""
QUESTION 2: FIND HOW MANY DIFFERENT TITLES THERE ARE, AND THEIR FREQUENCIES
"""


def differentTitles(facultyData):
	count = 0
	titleDict = dict()
	for row in facultyData:
		# print row
		title = row[2]
		if count > 0:
			if title not in titleDict:
				titleDict[title] = 1
			else:
				titleDict[title] += 1
		count += 1
	return titleDict

# print differentTitles(facultyData)


"""
QUESTION 3
"""

def differentEmails(facultyData):
	differentEmails = []
	count = 0
	for row in facultyData:
		# print row
		if row[3] not in differentEmails and count > 0:
			differentEmails.append(row[3])
		count += 1
	return differentEmails

emails = differentEmails(facultyData)

""" Question 4""" 

def differentDomains(emailList):
	emailDict = dict()
	for email in emailList:
		print email
		addr = email
		uname, domain = addr.split('@')
		if domain not in emailDict:
			emailDict[domain] = 1
		else:
			emailDict[domain] += 1
	print len(emailDict)
	return emailDict



print differentDomains(emails)








