# Justin Hummert
# JPH99@pitt.edu
# 10/12/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 5, Exercise 6

# This program takes the values for grams of fat and carbs and converts to calories from each


def calorie_calculator():
    calories_fat = fat * 9
    calories_carbs = carbs * 4
    print('The results are',calories_fat,'calories from fat and',calories_carbs,'calories from carbs.')
fat = float(input('How many grams of fat do you eat? '))
carbs = float(input('How many grams of carbs do you eat?' ))
calorie_calculator()