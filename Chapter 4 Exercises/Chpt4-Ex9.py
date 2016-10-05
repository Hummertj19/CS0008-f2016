# Justin Hummert
# JPH99@pitt.edu
#10/3/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 9

# Calculating number of mm's ocean will have risen each year and displaying that
year = 0
total = 0
for year in range(0, 25):
    total += 1.6
    print(format(total,'.2f'),'millimeters',)
