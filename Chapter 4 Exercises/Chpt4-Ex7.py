# Justin Hummert
# JPH99@pitt.edu
# 10/3/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 7

# Asking for the number of days
days = int(input('How many days? '))

# Calculating salary based on days entered
if days == 0:
    salary = 0
elif days == 1:
    salary = .01
else:
    ts = 0
    salary = 0.01
    for days in range(0, days):
        salary *= 2
        print(salary)
        ts += salary
print(format(ts,'.2f'))