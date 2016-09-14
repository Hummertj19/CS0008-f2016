# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 4

# Asking user to input number
number = int(input('Please enter a number 1 through 10'))

# Displaying roman numerals
if number == 1:
    print('I')
elif number == 2:
    print('II')
elif number == 3:
    print('III')
elif number == 4:
    print('IV')
elif number == 5:
    print('V')
elif number == 6:
    print('VI')
elif number == 7:
    print('VII')
elif number == 8:
    print('VIII')
elif number == 9:
    print('IX')
elif number == 10:
    print('X')
else:
    if number < 1:
        print('Error')
    elif number > 1:
        print('Error')