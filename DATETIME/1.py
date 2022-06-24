# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:54:51 2022

@author: Satya
"""

from datetime import datetime, date
now = date.today()
print('\n', 'Today is: ', now,
'\n', 'now Data Type:', type(now))


nl = '\n'
d1 = date(1960, 1, 2)
day = d1.day
month = d1.month
year = d1.year
print(nl, 'd1: ' , d1,
nl, 'd1 data type: ' , type(d1),
nl, 'day: ' , day,
nl, 'day data type: ' , type(day),
nl, 'month: ' , month,
nl, 'month data type:' , type(month),
nl, 'year: ' , year,
nl, 'year data type: ' , type(year))


d1 = date(1960, 1, 2)
d2 = date(2019, 7, 4)
dif = d2 - d1

d1 = datetime(year=2019, month =12, day=25)
dow1 = d1.weekday()

dow2 = d1.isoweekday()
iso_cal = date(2019, 12, 25).isocalendar()

print(nl, 'Day of Week:' ,dow1,
nl, 'ISO Day of Week:' ,dow2,
nl, 'ISO Calendar:' ,iso_cal)