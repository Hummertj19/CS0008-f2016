# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 5

# Asking user to enter mass
mass = int(input("What is the mass of the object?"))

# Calculating weight of objected entered
weight = mass * 9.8

# Displaying results
if mass < 100:
    print('Object is too light')
elif mass > 500:
    print('Object is too heavy')
else:
    print('Weight of object is',weight,'pounds.')