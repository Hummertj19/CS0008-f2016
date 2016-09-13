# Justin Hummert
# JPH99@pitt.edu
# 9/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 2, Exercise 10

# Asking the amount of cookies
cookies = int(input('How many cookies do you want to make?'))

# Calculating the amount of ingredients required
sugar = 300 * cookies
butter = 240 * cookies
flour = 330 * cookies

# Displaying the final answer
print('To make',cookies,'cookies you will need:')
print(sugar,'grams of sugar')
print(butter,'grams of butter')
print(flour,'grams of flour')