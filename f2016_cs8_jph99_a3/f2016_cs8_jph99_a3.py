#
# MN: header with user, intructor and course info is missing
#
# Notes:
#


# First I set the variable equal to the path of the file, then I opened the file and had it read all the lines, and
# take the 3 files in the text file and save them into memory
# MN: why not asking the user for the master list file name?
# MN: if you hard code the file path it makes it hard to test.
#datasources = '/Users/Hummertj19/Documents/CS0008/CS0008-f2016/CS0008-f2016/f2016_cs8_jph99_a3/f2016_cs8_a3/\
#f2016_cs8_a3.data.txt'
datasources = 'f2016_cs8_a3.data.txt'
fh = open(datasources, 'r')
sourceFiles = fh.readlines()
fh.close()
sourceFiles = [item.rstrip('\n') for item in sourceFiles]
# Here I set everything equal to 0, or made it empty so I could add to them later
data = []
dictionary = {}
filesread = 0
num_of_times_dict = {}
total_person_distance_dict={}
# I set up this for loop to read through all three files
for source in sourceFiles:
    fh = open(source, 'r')
    filesread += 1
    # I set up this for loop to read through all the lines in all 3 files
    for line in fh:
        # I did this to get rid of the header on each file
        if 'distance' not in line:
            # Here, I added everything to the data list and got rid of the new line character
            data.append(line.strip('\n'))
            # Here I found the total distance by summing the second item in the data list, after making them floats
            total_distance = sum([float(item.split(',')[1]) for item in data])
            # Here I created a dictionary out of the lines from the file
            key = line.split(',')[0]
            value = float(line.split(',')[1])
            dictionary[key]=value
            # This adds the number of times a key shows up and puts that as a value into num_of_times_dict
            # Also, it adds the run distance for every person for each run and uses that as a value for that specific key
            if key not in num_of_times_dict:
                total_person_distance_dict[key] = 0
                num_of_times_dict[key] = 0
            total_person_distance_dict[key]+=value
            num_of_times_dict[key]+=1
            # Here I found the max and min distances by running those respective functions, and then finding the key
            # associated with that value
            # MN: here you are performing these statements for every line read from each data file
            #     I'm quite sure that you could move them reide after these 2 loops, saving time and cpu cycles
            # MN: with this logic, you find the min and max on each single record/run,
            #     not the min and max on the total distance run by the participants
            maximum_distance = max([float(item.split(',')[1]) for item in data])
            max_runner = {v: k for k, v in dictionary.items()}[maximum_distance]
            minimum_distance = min([float(item.split(',')[1]) for item in data])
            min_runner = {v: k for k, v in dictionary.items()}[minimum_distance]
    fh.close()

# I found the number of people who ran more than once here
count=0
for person in num_of_times_dict:
    if num_of_times_dict[person]>1:
        count+=1

# This gets a list with each value in that list being a list containing the name, the number of times they ran, and the
# total distance that they ran
result_list=[]
for person in num_of_times_dict:
    num_of_times=num_of_times_dict[person]
    total_person_distance=total_person_distance_dict[person]
    put_together=[person,num_of_times,total_person_distance]
    result_list.append(put_together)

#This puts the list into a giant string so I can put it in a file
result_string=''
for line in result_list:
    line_name=line[0]
    line_repeat=line[1]
    line_distance=line[2]
    line_string='%s,%d,%f' % (line_name,line_repeat,line_distance)
    result_string+=(line_string)+'\n'
# This part creates a file and puts the final list into it
# MN: respect file naming conventions as requested by assignment
#new_file = open('results.txt','w')
new_file = open('f2016_cs8_jph99_a3.output.txt','w')
new_file.write(result_string)
new_file.close()


print('Number of input files read                  :',filesread)
print('Total number of lines read                  :',len(data))
print('Total distance ran                          :',total_distance)
print('Maximum distance ran                        :',maximum_distance)
print('By runner                                   :',max_runner)
print('Minimum distance ran                        :',minimum_distance)
print('By runner                                   :',min_runner)
print('Total number of participants                :','450')
print('Number of participants with multiple records:',count)