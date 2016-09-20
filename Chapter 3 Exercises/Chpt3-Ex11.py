# Justin Hummert
# JPH99@pitt.edu
# 9/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 11

# Asking the user to enter the amount of books purchased
books_bought = int(input('How many books did you buy?'))

# Calculating the number of points the user gets
if books_bought <= 1:
    print('You get 0 points.')
elif 1 < books_bought <= 3:
    print('You get 5 points.')
elif 3 < books_bought <= 5:
    print('You get 15 points.')
elif 5 < books_bought <= 7:
    print('You get 30 points.')
else:
    print('You get 60 points.')
