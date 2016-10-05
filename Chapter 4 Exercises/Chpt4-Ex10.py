# Justin Hummert
# JPH99@pitt.edu
# 10/5/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 10

# Calculating tuition for each semester by taking what it will be after each year and cutting it in half
tuition = 8000
year = 0
for year in range (5):
    tuition += (tuition*.03)
    print('$', format(tuition/2, ',.2f'), ' per semester.', sep='')
