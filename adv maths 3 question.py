# area of trapezioum
def a(b,c,h):
    if b==0 or c==0 or h==0:
        return 0
    return 0.5*(b+c)*h
print(a(5,7,4))
print(a(6,8,5))
print(a(10,15,8))
print(a(7,9,6))
print(a(0,5,5))
# area of sphere
import math
def ar(r):
    return 4*math.pi*r**2
print(ar(3))
print(ar(5))
print(ar(7))
print(ar(2))
print(ar(0))
# calcukation of discount
def f(p,d):
    return p-d*p/100
print(f(100,80))
print(f(200,15))
print(f(150,25))
print(f(50,10))
print(f(0,50))
# time difference
from datetime import datetime

def time_difference(time1, time2):
    # Define the time format
    time_format = "%H:%M"
    
    # Convert the time strings into datetime objects
    t1 = datetime.strptime(time1, time_format)
    t2 = datetime.strptime(time2, time_format)
    
    # If time2 is earlier than time1, adjust for the midnight crossover
    if t2 < t1:
        t2 += time_format(days=1)
    
    # Calculate the time difference
    time_diff = t2 - t1
    
    # Extract hours and minutes from the time difference
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    
    return f"{hours} hours, {minutes} minutes"

# Test cases
print(time_difference("10:30", "12:45"))  # Output: 2 hours, 15 minutes
print(time_difference("15:00", "18:30"))  # Output: 3 hours, 30 minutes
print(time_difference("09:15", "09:15"))  # Output: 0 hours, 0 minutes
print(time_difference("23:59", "00:01"))  # Output: 0 hours, 2 minutes
print(time_difference("12:00", "12:01"))  # Output: 0 hours, 1 minute
from datetime import datetime

def date_difference(date1, date2):
    # Define the date format
    date_format = "%Y-%m-%d"
    
    # Convert the date strings into datetime objects
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    
    # Calculate the difference in days
    day_diff = (d2 - d1).days
    
    # Return the difference in days, handling singular and plural
    if day_diff == 1:
        return "1 day"
    return f"{day_diff} days"

# Test cases
print(date_difference("2024-01-01", "2024-01-10"))  # Output: 9 days
print(date_difference("2024-02-28", "2024-03-01"))  # Output: 2 days
print(date_difference("2024-07-01", "2024-07-01"))  # Output: 0 days
print(date_difference("2023-12-31", "2024-01-01"))  # Output: 1 day
print(date_difference("2024-03-01", "2023-03-01"))  # Output: -366 days
