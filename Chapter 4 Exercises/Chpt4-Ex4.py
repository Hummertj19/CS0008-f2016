# Justin Hummert
# JPH99@pitt.edu
# 9/28/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 4

# Asking user in input speed and time
speed = int(input('What is the speed of the vehicle in mph?'))
time = int(input('How many hours has it travelled?'))

# Calculating and displaying distance for each hour
hour = 0
distance = 0
while hour < time:
    distance = (speed * time) + distance
    hour = hour + 1
    print('During hour',hour,'you traveled',distance,'miles.')
