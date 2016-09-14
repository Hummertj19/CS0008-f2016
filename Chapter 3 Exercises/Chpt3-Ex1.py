# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 1

# Asking the user to enter a number
day_of_week = int(input('Please enter a number, 1 through 7!'))

# Printing day based on number entered
if day_of_week == 1:
    print('Monday')
if day_of_week == 2:
    print('Tuesday')
if day_of_week == 3:
    print('Wednesday')
if day_of_week == 4:
    print('Thursday')
if day_of_week == 5:
    print('Friday')
if day_of_week == 6:
    print('Saturday')
if day_of_week == 7:
    print('Sunday')
if day_of_week < 1:
    print('Error')
if day_of_week > 7:
    print('Error')