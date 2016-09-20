# Justin Hummert
# JPH99@pitt.edu
# 9/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 12

# Asking the user how many packages they purchased
packes_purchased = int(input('How many packages did you buy?'))
cost_before_discount = packes_purchased * 99

# Calculating discount and displaying results
if packes_purchased < 10:
    print('Your total amount is:',cost_before_discount)
elif 10 <= packes_purchased <= 19:
    print('Your total amount is:',(cost_before_discount - (cost_before_discount * .1)))
elif 20 <= packes_purchased <= 49:
    print('Your total amount is:', (cost_before_discount - (cost_before_discount * .2)))
elif 50 <= packes_purchased <= 99:
    print('Your total amount is:', (cost_before_discount - (cost_before_discount * .3)))
elif packes_purchased >= 100:
    print('Your total amount is:', (cost_before_discount - (cost_before_discount * .4)))
