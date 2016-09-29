# Justin Hummert
# JPH99@pitt.edu
# 9/30/16
# CS0008-f2016
# Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment Number 1

# Asking user for USC or Metric, and then converting
system = (input('Enter + for USC or - for Metric units. '))
if system != '+':
    if system != '-':
        print('Error')
        quit()
if system == '+':
    distance_us = float(input('How far did you drive? '))
    gas_us = float(input('How much gas did you use? '))
    distance_metric = distance_us * 1.60934
    gas_metric = gas_us * 3.78541
    us_mpg = distance_us/gas_us
    metric_lpok = (100 * gas_metric)/distance_metric
else:
    distance_metric = float(input('How far did you drive? '))
    gas_metric = float(input('How much gas did you use? '))
    distance_us = distance_metric * 0.621371
    gas_us = gas_metric * 0.264172
    metric_lpok = (100 * gas_metric)/distance_metric
    us_mpg = distance_us/gas_us

# Displaying Data
print('              ','    USC','      Metric')
print('Distance     :', '{:>10.3f}'.format(distance_us), '{:>10.3f}'.format(distance_metric))
print('Gas          :', '{:>10.3f}'.format(gas_us), '{:>10.3f}'.format(gas_metric))
print('Consumption  :', '{:>10.3f}'.format(us_mpg), '{:>10.3f}'.format(metric_lpok))
