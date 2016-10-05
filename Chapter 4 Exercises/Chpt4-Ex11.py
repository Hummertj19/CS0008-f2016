# Justin Hummert
# JPH99@pitt.edu
# 10/5/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 11

# Asking user for number, asking for new number if number is negative
number = int(input('Enter a number: '))
while number < 0:
    print('Please enter a positive number.')
    number = int(input('Enter a number: '))

# Factorial is originally 1 because it will multiply each time by the next numbers in the sequence
factorial = 1

# The number entered and the one below it will be multiplied by the factorial, and the new number will be two below
# the original, this will continue for the entire factorial because it will stop once the number becomes less than 1
while number > 1:
    next_number = number - 1
    factorial *= (number * next_number)
    number -= 2
print(factorial)