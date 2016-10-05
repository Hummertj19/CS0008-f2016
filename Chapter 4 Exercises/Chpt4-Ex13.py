# Justin Hummert
# JPH99@pitt.edu
# 10/5/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 13

# Making a stair pattern going in descending order from 7
base_size = 7
for r in range(base_size, 0, -1):
    for c in range(r):
        print('*',end='')
    print()