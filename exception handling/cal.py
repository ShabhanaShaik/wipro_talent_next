#calendar module
#complete yr
"""
import calendar
year=int(input("enter a year number:"))
print(calendar.calendar(year))"""
#only month
"""from calendar import *
yr=int(input("enter yr:"))
mon=int(input("enter month num"))
str=month(yr,mon)
print(str)"""
#leap yr
"""from calendar import *
yr=int(input("enter yr:"))
if isleap(yr):
    print(f"{yr} is leap yr")
else:
    print(f"{yr} is not leap yr")"""
#print 10 da from today continously
"""from datetime import *
d=date.today()
print(d)
d= date(2005,1,1)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)
"""
#entire date is printed i.e,yr,date,mon,day in single line
"""import time
epoch=time.time()#gives time in secs from 1970 jan1 to present
print(epoch)
curr=time.ctime(epoch)#gives current time
print(curr)
"""