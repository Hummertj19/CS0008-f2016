# Justin Hummert
# JPH99@pitt.edu
# 10/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 8

# This program takes the area of the room and the current price of paint and calculates and displays the total price
# of the job, as well as the individual prices for everything needed.

area = int(input('Enter the square footage that needs painted: '))
paint = int(input('Enter the price of paint: '))


def price_calculator():
    base_unit = area//112
    cost_of_labor = base_unit * (35*8)
    cost_of_paint = base_unit * paint
    print('You will need',base_unit,'gallons of paint. You will need',(base_unit*8),'hours of labor. You will need',
        cost_of_paint,'dollars worth of paint. You will need',cost_of_labor,'dollars worth of labor. You will need',
        'as a total,',cost_of_labor + cost_of_paint,'dollars.')

price_calculator()