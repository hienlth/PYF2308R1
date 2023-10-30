# Write a Python program to display calendar?
import calendar

year = int(input("Enter year: "))

cal = calendar.calendar(year)
print("\n", cal)