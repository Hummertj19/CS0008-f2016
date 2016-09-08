# Justin Hummert
# JPH99@pitt.edu
# 9/8/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 2, Exercise 7

miles = int(input('How many miles did you drive?'))
gas = int(input('How many gallons of gas did you use?'))
kilometers = miles * 1.60934
liters = gas * 3.78541
liters_per_100km = 100 * (liters/kilometers)
print("Kilometers driven:", kilometers)
print('Liters used:',liters)
print('Liters per 100km:', liters_per_100km)