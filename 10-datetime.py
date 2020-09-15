from datetime import datetime, date
import time
from datetime import datetime, date, time, timedelta
now = datetime.now()
print(now)
print(date.today())
custom_date = datetime(year=2020,month=9,day=15,hour=20,minute=30,second=30)
print(custom_date)
print(type(custom_date))
custom_date = custom_date.strftime("%Y/%m/%d %I:%M:%S %p")
print(custom_date)
print(type(custom_date))
now = datetime.now()

today = datetime.now()
print(today+timedelta(days=-1))
