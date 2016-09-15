# Justin Hummert
# JPH99@pitt.edu
# 9/15/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 9

# Asking for the number
number = int(input('Give me the number'))

# Testing if the number is out of the range
if not (number >= 0 and number <= 36):
    print('Give me a number ')

# Testing the range and determining the color
elif number == 0:
    color = 'green'
elif (number >= 1 and number <= 10) \
      or \
     (number >= 19 and number <= 28):
    if number % 2 == 0:
        color = 'black'
    else:
        color = 'red'
elif (number >= 11 and number <= 18) \
      or \
     (number >= 28 and number <= 36):
    if number % 2 == 0:
        color = 'red'
    else:
        color = 'black'
print(color)
