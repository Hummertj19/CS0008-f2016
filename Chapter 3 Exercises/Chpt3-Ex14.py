# Justin Hummert
# JPH99@pitt.edu
# 9/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 14

# Asking user to input height and weight
weight = int(input('How much do you weigh? (Pounds) '))
height = int(input('How tall are you? (Inches) '))

# Calculating BMI
body_mass_index = weight * (703/(height**2))

# Displaying Results
print('Your BMI is:',body_mass_index)
if 18.5 <= body_mass_index <= 25:
    print('Your BMI is optimal.')
elif body_mass_index < 18.5:
    print('You are underweight.')
else:
    print('You are overweight.')