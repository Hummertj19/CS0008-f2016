# Justin Hummert
# JPH99@pitt.edu
#10/3/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 8

# Asking user to enter the number and calculating the total, stopping the program if a negative number is entered
y = 0
total = 0
while y == 0:
    number = int(input('Enter a number. '))
    if number < 0:
        y = 1
    else:
        total += number
print(total)
