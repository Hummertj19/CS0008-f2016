# Justin Hummert
# JPH99@pitt.edu
# 10/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 11

# This program takes 2 random numbers and asks the user for their sum, if the user's answer is correct,
# it will say good job. If not, it will tell the user he is wrong and show the correct answer.

import random


def addition_test():
    number1 = random.randint(1, 10000)
    number2 = random.randint(1, 10000)
    answer = number1 + number2
    print(number1,'+',number2)
    solution = int(input('Enter the answer: '))
    if answer != solution:
        print('Incorrect, the answer is:', answer)
    elif answer == solution:
        print('Good job')

addition_test()
