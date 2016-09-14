# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 2

# Asking for length and width of each rectangle
width_1 = int(input('Please enter the width of Rectangle 1'))
length_1 = int(input('Please enter the length of Rectangle 1'))
width_2 = int(input("Please enter the width of Rectangle 2"))
length_2 = int(input('Please enter the length of Rectangle 2'))

# Calculating the areas of the 2 rectangles
area_1 = width_1 * length_1
area_2 = width_2 * length_2

# Telling the user about the areas
if area_1 > area_2:
    print('Rectangle 1 has a greater area than Rectangle 2')
else:
    if area_2 > area_1:
        print('Rectangle 2 has a greater area than Rectangle 1')
    else:
        if area_1 == area_2:
            print('The Recatangles have the same area')

