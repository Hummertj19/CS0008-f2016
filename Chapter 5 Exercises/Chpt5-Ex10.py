# Justin Hummert
# JPH99@pitt.edu
# 10/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 10

# Program accepts a number of feet and uses a function to turn that into inches


def feet_to_inches():
    inches = feet * 12
    return inches

feet = int(input('Enter the number of feet: '))

print(feet_to_inches(),'inches')
