# Justin Hummert
# JPH99@pitt.edu
# 9/19/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 10

# Asking the user for the amount of coins
pennies = int(input('Pennies?'))
nickels = int(input('Nickels?'))
dimes = int(input('Dimes?'))
quarters = int(input('Quarters?'))

# Calculating the amount entered
cents_p = pennies
cents_n = nickels * 5
cents_d = dimes * 10
cents_q = quarters * 25
total = (cents_d + cents_n + cents_p + cents_q)
# Returning results to user
print(total, 'cents')
if total == 100:
    print("Congrats on winning!!")
elif total < 100:
    print("You didn't enter enough!")
else:
    print("You entered too much!!")