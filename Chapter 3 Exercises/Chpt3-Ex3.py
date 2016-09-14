# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 3

# Asking user to input their age
age = int(input('Please enter your age'))

# Displaying message
if age <= 1:
    print('Infant')
elif 1 < age < 13:
    print('Child')
elif 13 <= age < 20:
    print('Teenager')
else:
    if age >= 20:
        print('Adult')