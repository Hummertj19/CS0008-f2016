# Justin Hummert
# JPH99@pitt.edu
# 10/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 9

# This program takes the total sales for a month at a company and calcualtes both the state and county taxes and
# displays them.

total_sales = float(input('Enter the total sales for the month: '))


def tax_calculator ():
    total = state_tax() + county_tax()
    print('The state tax is',state_tax(),'dollars, the county tax is',county_tax(),'the total is',total,'.')


def state_tax():
    value = total_sales * (0.025)
    return value


def county_tax():
    value = total_sales * (0.5)
    return value

tax_calculator()