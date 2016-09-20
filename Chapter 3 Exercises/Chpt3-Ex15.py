# Justin Hummert
# JPH99@pitt.edu
# 9/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 15

# Asking the user to enter an amount of seconds
seconds = int(input('Seconds: '))

# Calculating and displaying seconds, minutes, hours, days
if seconds < 60:
    print(seconds, 'seconds')
elif 60 <= seconds < 3600:
    print(seconds // 60, 'minutes')
elif 3600 <= seconds < 86400:
    print(seconds // 3600, 'hours')
else:
    print(seconds // 86400, 'days')
