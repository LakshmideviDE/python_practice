import datetime
current_date=datetime.datetime.now()
print("current date",current_date)
new_date=current_date+datetime.timedelta(hours=2)
print(new_date)
#we can also modify the week and days also
import datetime
current_date=datetime.datetime.now()
print("current date",current_date)
new_date=current_date+datetime.timedelta(weeks=2,days=3)
print(new_date)