# The first thing I did was create and define the class runners
class runner:
    # Then I set all these to 0 because they aren't known yet
    name = "unknown"
    distance = 0
    runs = 0
    # The next step was to use the initializer method to initialize the data
    def __init__(self, name, distance=0):
        self.name = name
        if distance > 0:
            self.distance = distance
            self.runs = 1
    # I defined the rest of the methods after the initializer, starting with the add distance method, which adds the
    # distance to the accumulator
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
    # This method adds multiple distances to the distance accumulator
    def addDistances(self, distances):
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
    # This method returns the name of the runner
    def getName(self):
        return self.name
    # This one returns the distance ran by the participant
    def getDistance(self):
        return self.distance
    # This method returns the number of runs the participant had
    def getRuns(self):
        return self.runs
    # This one turns the data into a string and returns all of it
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
    # This last method returns the values as csv's
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

# I defined this function to read the files in the master file and date the data from them
def read_file(file):
    # Here I created a blank list to put the data in
    result_list = []
    # This cycles through all the lines in the file
    for line in open(file , 'r'):
        # Here the header is skipped, because we know the word distance is in it
        if "distance" not in line:
            # Right here I took the new line off of the end and also split the values at the comma
            temporary_value = line.rstrip('\n').split(',')
            # Here I took the split name and added it to the result list, without the space, and then added the distance
            # in the same fashion, and also converted the distance to a float
            result_list.append({'name': temporary_value[0].strip(' '), 'distance' : float(temporary_value[1])})
    # This function returns  result lists of all the files
    return result_list
# Here I ask the user to enter the master file
masterFile = input("Please enter the full path of the master file: ")
# Next, I opened the master file to read, and removed the new line character
dataFiles = [file.rstrip('\n') for file in open(masterFile , 'r')]
# Here I made an empty list called raw data
raw_data = []
# Then I looped through the files and added them to the empty list, using one of the ways we were given by Max
for file in dataFiles:
    for item2 in read_file(file):
        raw_data.append(item2)
# The number of files, aka the number of files read, is the length of the data files list, which is 3
numberFiles = len(dataFiles)
# The number of total lines read is equal to the length of the raw data, which is every line of ever file except for
# the headers
totalLines = len(raw_data)
# The total distance run is just the sum of all the distances in the raw_data list
totalDistanceRun = sum([item['distance'] for item in raw_data])
# Here I created an empty dictionary called runners
runners = {}
# Here I used a for loop to loop through all of the lines in the file, and if a name is new, it adds it to the
# dictionary I created
for item in raw_data:
    if not item['name'] in runners.keys():
        runners[item['name']] = runner(item['name'])
    runners[item['name']].addDistance(item['distance'])
# Here I initialized the min and max distance variables
minDistance = { 'name' : None, 'distance': None }
maxDistance = { 'name' : None, 'distance': None }
# I then created an empty dictionary to calculate how many times each person ran
appearances = {}
# This for loop runs through the entire list of runners and figures out their total distance run
for name, object in runners.items():
    # The distance variable is just equal to the total distance ran by a runner
    distance = object.getDistance()
    # This will created a new min distance and name every time it finds a new lower distance, until it finds the lowest
    # and that will be the name and distance that it return
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # This does the same thing as the min distance if statement except it finds the highest total distance instead of
    # the lowest total distance
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance
    # This gets the total number of times that each runner was in the files
    times_runner_appeared = object.getRuns()
    # This checks if we need to initialize this entry, I got this part from the file shared with us
    if not times_runner_appeared in appearances.keys():
        appearances[times_runner_appeared] = []
        appearances[times_runner_appeared].append(name)
# The total number of participants is just the length of the list of all the runners
total_participants = len(runners)
# The number of participants who appeared more than one time is just the number of people who had the value of
# getRuns > 1
participants_who_appeared_more_than_once = len([1 for item in runners.values() if item.getRuns() > 1])
# Here I displayed the final results of the program
print(" Number of Input files read   : " + format(numberFiles,'5d'))
print(" Total number of lines read   : " + format(totalLines,'5d'))
print(" Total distance run           : " + format(totalDistanceRun,'12.5f'))
print(" Max distance run             : " + format(maxDistance['distance'],'12.5f'))
print("   by participant             : " + format(maxDistance['name'],'20s'))
print(" Min distance run             : " + format(minDistance['distance'],'12.5f'))
print("   by participant             : " + format(minDistance['name'],'20s'))
print(" Total number of participants : " + format(total_participants,'5d'))
print(" Number of participants")
print("  with multiple records       : " + format(participants_who_appeared_more_than_once,'12.5f'))
# Here I created the output file the the project called for and opened it to write
fh = open('f2016_cs8_jph99_fp.data.output.csv','w')
# Then I added all of the data, being the name, # of times ran, and total distance
for name, object in runners.items():
    # After adding each thing and turning it into a csv using the method from above, I added a newline and then closed
    # the file at the end
    fh.write(object.tocsv() + '\n')
fh.close()