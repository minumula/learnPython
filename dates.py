from datetime import datetime, timedelta

today = datetime.now()
print ('Today is ' + str(today))

one_week =timedelta(weeks=1)
lastweek = today - one_week

print ('Last Week was ' + str(lastweek))

print ('day: ' + str(today.day))
print ('Month '+ str(today.month))
print ('Year '+ str(today.year))


print ('Hour: ' + str(today.hour))
print ('Minute '+ str(today.minute))
print ('Second '+ str(today.second))


birthday = input ('when is your birthday (mm/dd/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%m/%d/%Y')
print ('Birthday: ' + str(birthday_date))