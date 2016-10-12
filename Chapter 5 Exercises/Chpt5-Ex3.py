# Justin Hummert
# JPH99@pitt.edu
# 10/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 3

# The program creates a function that calculates the insurance somebody should buy for their property


def insurance_finder():
    insurance = property * 0.8
    print('You should buy',insurance,'dollars worth of insurance.')

property = int(input('How much is the propert worth? '))
insurance_finder()