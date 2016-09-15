# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 7

# Ask the user to enter the two colors
color_1 = input('Enter color 1')
color_2 = input('Enter color 2')

# Displaying what colors will be produced
if color_1 == 'blue':
    if color_2 == 'red':
        print('purple')
    elif color_2 == 'yellow':
        print('green')
    else:
        print('Error')
elif color_1 == 'red':
    if color_2 == 'blue':
        print('purple')
    elif color_2 == 'yellow':
        print('orange')
    else:
        print('Error')
elif color_1 == 'yellow':
    if color_2 == 'red':
        print('orange')
    elif color_2 == 'blue':
        print('green')
    else:
        print('Error')
else:
    print('Error')