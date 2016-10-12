# Justin Hummert
# JPH99@pitt.edu
# 10/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 5

# This program takes the value of property and returns the assessment value and the property tax


def tax_calculator():
    assessment_value = 0.60 * actual_value
    property_tax = (assessment_value//100) * 0.72
    print('The assessment value of your property is',assessment_value,'dollars, and the property tax is',
          format(property_tax,'.2f'),'dollars')
actual_value = float(input('How much is your property worth? '))
tax_calculator()
