# Justin Hummert
# JPH99@pitt.edu
# 10/28/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment Number 2

# The idea of this program is to take .csv files and add up the total number of lines, as well as the distance ran,
# which is the second value in the file.

# First, I will define the process file, and define the file opened as the distance_file
def process_file(fh):
    distance_file = open(fh, 'r')
    # I set the partials to 0 to begin with
    partial_lines = 0
    partial_distance = 0
    # Then I call the for loop to read through all the lines of the file
    for line in distance_file:
        # The partial lines is augmented to add 1 after each loop, to calculate the total number of lines
        partial_lines += 1
        # The temporary value below is the value of each line of the file after it is separated
        temp = line.split(',')
        # Then, I assign distance to the second value of teach line, and add it to the running total each loop
        distance = float(temp[1])
        partial_distance += distance
    # After the for loop has gone through the file, the file is closed and the function returns the two values below
    distance_file.close()
    return partial_lines, partial_distance

# Here I set the totals to 0, and defined file_object as the name of the file entered by the user
total_lines = 0
total_distance = 0
file_object = input('First file: ')
# Here I set up the while loop so the program would repeat until the user enters one of the 3 key words to stop it
while file_object != '' and file_object != 'quit' and file_object != 'q':
    # I defined x and y as the two partial values returned by the function 'process_file'
    x, y = process_file(file_object)
    # Then I had the program display the results of each file
    print('File to be read                  :', file_object)
    print('Partial total # of lines         :', x)
    print('Partial total distance ran       :', format(y, '.3f'))
    # Here the program keeps a running total of the totals, so after each file it adds the values to the running total
    total_lines += x
    total_distance += y
    # After the program has ran through, it asks the user to enter the name of the next file
    print('')
    file_object = input('Next file: ')

# Once the program is finished, the totals are displayed in a table
print('')
print('Totals')
print('Total number of lines            :', total_lines)
print('Total distance ran               :', format(total_distance, '.3f'))