import datetime 
date=str(input())
day_name= ['Thursday', 'Friday', 'Saturday','Sunday','Monday','Tuesday','Wednesday']
#giving the day to enum from which day to start
#weekday() function returns an integer corresponding to the day of a week
day = datetime.datetime.strptime(date, '%d %m').weekday()
print(day_name[day])
