"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import date


today = str(date.today())
default_year = today[0:4]
default_month = today[5:7] if int(today[5:7]) > 9 else today[6:7]
default_day = today[8:10] if int(today[8:10]) > 9 else today[9:10]


if len(sys.argv) == 1:
	print(calendar.monthcalendar(int(default_year), int(default_month)))
elif len(sys.argv) == 2:
	mo = sys.argv[1]
	print(calendar.monthcalendar(int(default_year), int(mo)))
elif len(sys.argv) == 3:
	yr = sys.argv[2]
	mo = sys.argv[1]
	print(calendar.monthcalendar(int(yr), int(mo)))

