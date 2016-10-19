# Justin Hummert
# JPH99@pitt.edu
# 10/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 7

#This program asks the user to enter the 3 amount of tickets bought and then returns the amount of money earned from
# ticket sales.


def ticket_counter():
    A = x * 20
    B = y * 15
    C = z * 10
    total = A + B + C
    return total

x = int(input('How many tickets in Class A? '))
y = int(input('How many tickets in Class B? '))
z = int(input('How many tickets in Class C? '))

print('You will receive',ticket_counter(),'dollars from ticket sales.')