# Justin Hummert
# JPH99@pitt.edu
# 10/5/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 12

# Asking the user to enter the starting organisms, percent increase, and days to multiply
organisms = int(input('Starting number of organisms: '))
increase = float(input('Average daily increase: '))
days = int(input('Number of days to multiply: '))

# The new total starts as the original number of organisms, but exponentially increases each day
new_total = organisms

# The first day it will always be the starting number of organisms
print('1',organisms)

# Calculating the number of organisms after the first day, up until the end of the range
for days in range(2,days+1):
    new_total *= (1+(increase/100))

    # Displaying data
    print(days,format(new_total,'.2f'))