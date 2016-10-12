# Justin Hummert
# JPH99@pitt.edu
# 10/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 2

# Creating a function to find the state and county tax of a purchase


def tax():
    state_tax = purchase * .05
    county_tax = purchase * .025
    total_tax = state_tax + county_tax
    print(state_tax,county_tax,total_tax,purchase + total_tax)

purchase = int(input('How much did the item cost? '))
tax()
