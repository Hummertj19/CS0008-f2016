# Justin Hummert
# JPH99@pitt.edu
# 9/28/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 4, Exercise 1

# Collecting # of bugs collected and adding it to the total
rt = 0
days = 1
while days < 6:
    bugs = int(input("How many bugs did you collect?"))
    rt = rt + bugs
    days = days + 1
print('You collected',rt,'bugs.')