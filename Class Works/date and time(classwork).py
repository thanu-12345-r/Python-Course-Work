from datetime import date,time

today=date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())


from datetime import date,time,datetime

now=datetime.now()
print(now)

print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("hour:",now.hour)
print("minute:",now.minute)
print("second:",now.second)


from datetime import date,time,datetime

now=datetime.now()

print(now.strftime('%d/%m/%y'))
print(now.strftime('%H/%M/%S'))
print(now.strftime('%I/%M/%S'))

print(now.strftime('%A, %d %b %y %I:%M:%S %p'))


from datetime import date,time,datetime,timedelta

today=date.today()
now=datetime.now()

n=today - timedelta(days=5)
print(n)

h=now - timedelta(hours=15)
print(h)


import sys

print("start")


import math

print(math.pow(2,4))
print(math.sqrt(64))
print(math.ceil(12.0001))
print(math.floor(12.0001))
print(math.fabs(12.0001))
print(math.factorial(5))
print(math.gcd(12,24))
print(math.sin(30))
print(math.radians(90))




