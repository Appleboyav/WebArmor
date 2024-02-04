from datetime import datetime

now = datetime.now().time().strftime("%H:%M:%S") # time object
date = datetime.now().strftime("%Y-%m-%d") # date object
print("date:",date)
print("time =", now)
print(datetime.now().strftime("%d-%m-%Y"))
print(datetime.now().strftime("%H:%M:%S"))
