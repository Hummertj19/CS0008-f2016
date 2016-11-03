# Justin Hummert
# JPH99@pitt.edu
# 11/3/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Programming Exercise 2

# First I had the user enter 2 numbers to have the operations done on them
number_one = int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))
# Then I set y equal to zero so I could use it to eventually end the while loop
y = 0
while y < 3:
    # In the while loop, I performed all of the operations, and made sure it would iterate three times, then printed
    addition = number_one + number_two
    subtraction = number_one - number_two
    multiplication = number_one * number_two
    intdivison = number_one//number_two
    floatdivision = number_one/number_two
    print(addition,subtraction,multiplication,intdivison,floatdivision)
    # At the end, I added one to y so that the while loop would stop after 3 iterations
    y += 1
