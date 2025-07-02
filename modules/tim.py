#datetime
"""datetime.now-->fetches system datetime
datetime.strptime-->fetches time as String 
datetime.strftime-->fetches in string format Time 
"""
from datetime import datetime,date,timedelta
now=datetime.now()
print("current datetime",now)
print("todays date",date.today())
#formatted date and time
formatted_time=date.today().strftime("%d-%m-%y %H:%M:%S")
print("formatted date and time",formatted_time)
#parsed datetime
date_str="24-12-2005 13:55:00"
parsed=datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")
print("parsed data",parsed)
#timedelta
tomm=now+timedelta(days=1)
print("tomorrow",tomm)
yes=now+timedelta(days=-1)
print("yesterdays",yes)
#future time
ftime=now+timedelta(hours=3,minutes=30)
print("after 3 and half hrs",ftime)
#format time for 12 hrs
"""%I=0-12
%p=AM/PM 
%H-0->23.59.59.00000"""
format_12hr=now.strftime("%I:%M:%p")
print(format_12hr)
format_24hr=now.strftime("%H:%M")
print(format_24hr)