# Justin Hummert
# JPH99@pitt.edu
# 9/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 13

# Asking user for weigh of package
weight_of_package = float(input('How much does the package weigh? '))

# Figuring out price of package
if weight_of_package <= 2:
    print('Your total is $',weight_of_package * 1.5)
elif 2 < weight_of_package <= 6:
    print('Your total is $', weight_of_package * 3)
elif 6 < weight_of_package <= 10:
    print('Your total is $', weight_of_package * 4)
elif weight_of_package > 10:
    print('Your total is $', weight_of_package * 4.75)
