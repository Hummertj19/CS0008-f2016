# Justin Hummert
# JPH99@pitt.edu
# 9/28/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 3

# Asking user to enter budget
budget = float(input('What is your budget for the month?'))

# Collecting expenses and calculating budget
x = '+'
expense = 0
while x == '+':
    expense = expense + float(input('Enter your expense.'))
    x = input('Enter + if you have more expense to enter, and - if not.')
total = budget - expense
if total > 0:
    print('You are',total,'dollars under budget.')
else:
    print('You are',total,'dollars over budget.')