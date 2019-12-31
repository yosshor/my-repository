import calendar
import datetime


print(datetime.datetime.today())
enter_date = input("enter a date :")
repl = enter_date.replace('/', ',')
t = repl[0:2]
t1 = repl[3]
t2 = repl[5]
print("{},{},{}".format(t,t1,t2))

print(datetime.datetime(enter_date))
print(datetime.datetime.today())
print(repl.year)
print(calendar.weekday())
print(repl)
