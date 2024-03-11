import datetime
res=datetime.datetime.now()
res1=datetime.datetime(2024,4,12)
print(res1)

#short version of current year
import datetime
cd=datetime.datetime.now()
res2=cd.strftime("%y")
print("short version of the year",res2)
res2=cd.strftime("%A")
print("full version of the day",res2)