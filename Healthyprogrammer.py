from datetime import datetime,timedelta
s = '09:00:00'
mytime = datetime.time.__str__(s, "%H:%M:%S")
mytime += timedelta(hours=6)
print(mytime.strftime("%Y.%m.%d %H:%M:%S"))

