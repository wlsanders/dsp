# Hint:  use Google to find python function

####a) 
#from datetime import datetime
from datetime import datetime
def days_between1(a,b):

	date_start = datetime.strptime(a, "%m-%d-%Y")    
	date_stop = datetime.strptime(b, "%m-%d-%Y")
	return abs((date_start - date_stop).days)


a = '01-02-2013'
b= '07-28-2015'
print days_between1(a,b), "days" 

####b)  
def days_between2(date_start, date_stop):
	a = datetime.strptime(date_start, "%m%d%Y")
	b = datetime.strptime(date_stop, "%m%d%Y")
	return abs((a - b).days)

date_start = '12312013'  
date_stop = '05282015'  
print days_between2(date_start,date_stop), "days"

####c)  
def days_between3(d1,d2):

	date_start = datetime.strptime(d1, "%d-%b-%Y")    
	date_stop = datetime.strptime(d2, "%d-%b-%Y")
	return abs((date_start - date_stop).days)


date_start3 = '15-Jan-1994'      
date_stop3 = '14-Jul-2015'  
print days_between3(date_start3, date_stop3), "days"