'''import calendar
year=int(input("Enter a year number: "))
print(calendar.calendar(year))'''

from calendar import *
year=int(input("Enter the year: "))
Month = int(input("Enter the month number:"))
str=month(year , Month)
print(str)