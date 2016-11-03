# Justin Hummert
# JPH99@pitt.edu
# 11/3/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Programming Exercise 16

# The function takes the two numbers and performs all of the operations on them


def number_function(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x//y)
    print(x**y)

# Here, it asks the user to enter the two numbers and uses them as the 2 arguments for the function
number_function(int(input('Enter the first number:')),int(input('Enter the second number: ')))
