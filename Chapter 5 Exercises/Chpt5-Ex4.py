# Justin Hummert
# JPH99@pitt.edu
# 10/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 4

# This program creates a function that calculates monthly and yearly expenses for car


def expense_calculator():
    monthly = loan + insurance + gas + oil + tires + maintenance
    annually = monthly * 12
    print('You pay',monthly,'dollars per month, and',annually,'dollars per year.')

loan = float(input('How much do you pay for loan? '))
insurance = float(input('How much do you pay for insurance? '))
gas = float(input('How much do you pay for gas? '))
oil = float(input('How much do you pay for oil? '))
tires = float(input('How much do you pay for tires? '))
maintenance = float(input('How much do you pay for maintenance? '))
expense_calculator()
