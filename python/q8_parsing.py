
import csv
exampleFile = open('football.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)


def BiggestTeamDifference(exampledata):
	count = 0
	BiggestDiffTeam = ""
	SmallestDiff = 100
	teamDiff = 0
	for row in exampleData:
		if count > 0:
			# print row[5], row[6], row[0]
			goalsFor = int(row[5])
			goalsAgainst = int(row[6])
			teamDiff =  goalsFor - goalsAgainst
			if teamDiff <= SmallestDiff:
				BiggestDiffTeam = row[0]
				SmallestDiff = teamDiff
		count += 1
	return BiggestDiffTeam, SmallestDiff

BiggestTeamDifference(exampleData)






