def a(c,add):
    r=''
    # d=ord(c)
    for char in c:
        d=ord(char)
        if d>65 and d<91:
            u=(d-65+add)%26+65
            r+=chr(u)
        elif d>97 and d<123:
            u=(d-97+add)%26+97
            r+=chr(u)
        else:
            r+=d
    return r
print(a('hello',3))
from datetime import datetime
def days_calc(d1, d2):
    date1 = datetime.strptime(d1, '%Y-%m-%d')  # Convert the first date string to a datetime object
    date2 = datetime.strptime(d2, '%Y-%m-%d')  # Convert the second date string to a datetime object
      # Calculate the absolute difference in days
    return abs((date2 - date1).days)
# Example usage
print(days_calc('2025-11-29', '2024-11-29'))
