

# date time program in Python
    
    
from datetime import date
import calendar
my_date = date.today()
print(my_date)

print(calendar.day_name[my_date.weekday()])

output =>

$python3 main.py
2019-03-16
Saturday