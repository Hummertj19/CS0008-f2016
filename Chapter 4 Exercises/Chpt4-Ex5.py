# Justin Hummert
# JPH99@pitt.edu
# 10/3/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 5

# Asking the user to input years and calculating total months
years = int(input('How many years have passed? '))
total_months = years * 12

# Creating the loop and asking for rainfall for each month
for years in range(1, years+1):
    tr = 0
    months = 12
    while months > 0:
        months -= 1
        rainfall = int(input('How much did it rain this month? '))
        tr += rainfall

# Displaying data
print('It has been',total_months,'months.')
print('The total amount of rainfall is',tr,'inches.')
print('The average amount of rainfall is',tr/total_months,'inches.')
