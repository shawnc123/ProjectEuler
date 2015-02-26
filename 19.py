import datetime

d = datetime.date(1901, 1, 1)
print d

ct = 0
while d.year < 2001:
    print d, d.weekday, d.day
    if d.weekday() == 6 and d.day == 1:
	ct += 1
    d += datetime.timedelta(days=1)

print ct
