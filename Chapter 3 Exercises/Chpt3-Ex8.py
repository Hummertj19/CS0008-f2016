# Justin Hummert
# JPH99@pitt.edu
# 9/14/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Starting with Python, Chapter 3, Exercise 8

# Ask for the number of people attending and the number of hot dogs they'll get
number_of_people = int(input('How many people will be attending?'))
number_of_hot_dogs_to_each_person = int(input('How many hot dogs will each person get?'))

# Calculating hot dogs and buns required, as well as leftovers
hot_dog_pack = 10
bun_pack = 8
hot_dogs_needed = number_of_people * number_of_hot_dogs_to_each_person
print('You need', hot_dogs_needed, 'hot dogs.')
packs_needed = hot_dogs_needed // 10
if packs_needed != 0:
    print('You will need', packs_needed + 1, 'packs of hot dogs.')
    print('You will have', (((packs_needed + 1) * 10) - (hot_dogs_needed)), 'hot dogs remaining.')
else:
    print('You will need', packs_needed, 'packs of hot dogs.')
    print('You will have', ((packs_needed * 10) - hot_dogs_needed), 'hot dogs remaining.')
packs_of_buns_needed = hot_dogs_needed // 8
if packs_of_buns_needed != 0:
    print('You will need', packs_of_buns_needed + 1, 'packs of buns.')
    print('You will have', ((packs_of_buns_needed + 1) * 8) - hot_dogs_needed,'buns left.')
else:
    print('You will need', packs_of_buns_needed, 'packs of buns.')
    print('You will have', ((packs_of_buns_needed) * 8) - hot_dogs_needed,'buns left.')