# 
import csv
facultyFile = open('faculty.csv')
facultyReader = csv.reader(facultyFile)
facultyData = list(facultyReader)

emailData = []
count = 0
for row in facultyData:
	if count > 0:

		emailData.append(row[3])
	count += 1


import csv
with open('emails.csv', 'w') as facultyData:
	facultyFileWriter = csv.writer(facultyData)
	facultyFileWriter.writerow(emailData)


emailFile = open('emails.csv')
emailReader = csv.reader(emailFile)
emailData = list(emailReader)

for row in emailData:
	print row