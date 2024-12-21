# a=('99hi')
# print(type(a))
# def g(a,b):
#     return (a-b)
# c=g(55,9)
# print(c)
# print(2**53)
# a='False'
# print(type(a))
# a=5
# b=4
# print(a!=b)
# print(ord('h'))
# print(10%26+97)
# print(chr(107))
# # print(10%26)
# print(7%26)
# import math
# number = 4.2
# # ceiling_number = math.ceil(number)
# print(math.ceil(number))  # Output: 5
# a='t:m::::l'
# print(a.split(':'))
# for x in range(3):
#     for y in range (2):
#         for z in range (1):
#             print(x,y,z)
# n=50
# for i in range (10):
#     v=i//2
#     print(v)
# for i in range (100,0,-1):
#     for j in range (100,0,2):
#         print(j)
# print((5*8)/10)
# import math
# print(math.sqrt(289))
# a=4.578
# # it will take given no of decimals which if after cama(",")
# print(round(5.4436,3))
# from datetime import datetime

# def calculate_days(date1: str, date2: str) -> int:
#     # Parse the input strings into datetime objects
#     date_format = "%Y-%m-%d"
#     d1 = datetime.strptime(date1, date_format)
#     d2 = datetime.strptime(date2, date_format)
    
#     # Calculate the absolute difference in days
#     delta = abs((d2 - d1).days)
    
#     return delta

# # Test cases
# print(calculate_days("2024-01-01", "2024-01-10"))  # Output: 9
# print(calculate_days("2024-12-31", "2025-01-01"))  # Output: 1
# print(calculate_days("2024-02-28", "2024-03-01"))  # Output: 2
# print(calculate_days("2023-09-18", "2024-09-18"))  # Output: 366
# print(calculate_days("2024-09-18", "2024-09-10"))  # Output: 8






# def calculate_days(start_date, end_date):
#     """
#     Calculate the number of days between two dates.

#     Parameters:
#     start_date (str): The first date in 'YYYY-MM-DD' format.
#     end_date (str): The second date in 'YYYY-MM-DD' format.

#     Returns:
#     int: Absolute number of days between the two dates.
#     """
#     from datetime import datetime

#     # Define the date format
#     date_format = "%Y-%m-%d"

#     # Parse each date using the format
#     d1 = datetime.strptime(start_date, date_format)  # Convert start_date to datetime
#     d2 = datetime.strptime(end_date, date_format)    # Convert end_date to datetime
    
#     # Calculate and return the absolute difference in days
#     return abs((d2 - d1).days)

# # Test cases
# print(calculate_days("2024-01-01", "2024-01-10"))  # Output: 9
# print(calculate_days("2024-12-31", "2025-01-01"))  # Output: 1
# print(calculate_days("2024-02-28", "2024-03-01"))  # Output: 2
# print(calculate_days("2023-09-18", "2024-09-18"))  # Output: 366
# print(calculate_days("2024-09-18", "2024-09-10"))  # Output: 8



def u(v,w):
    if v is True and w=='false' or w=='true':
        return 'true'
    elif v=='false' and w=='true':
        return 'true'
    else:
        return 'false'
print(u('true','true'))
print(u('true','false'))
print(u('false','false'))
print(u('false','true'))
print(u('false','false'))

z=10
if z>=10:
    print('l')
elif z>=9:
    print('m')
else:
    print('n')