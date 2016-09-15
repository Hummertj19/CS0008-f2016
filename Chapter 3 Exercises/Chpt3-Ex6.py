# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 6

# Ask user to enter the day, month, and year
month = int(input('Enter a month'))
day = int(input('Enter a day'))
year = int(input('Enter a year'))

# Determine whether the month times the day equals the year
if month * day == year:
    print('Magic')
else:
    print('Date is not magic')