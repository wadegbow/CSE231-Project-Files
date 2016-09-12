# Project 2
# using inputs of length, depth and distance between plants
# output number of plants needed and volume of soil and fill
import math

# set constants
pi = math.pi

# get user inputs
length = \
    float(input('Please enter the side length for your garden (in feet):'))
distance = \
    float(input('Please enter the distance between plants (in inches):'))
depth_flow = \
    float(input('Please enter the depth for the flower beds (in feet):'))
depth_fill = \
    float(input('Please enter the depth for the fill (in feet):'))

# the length is the diameter of 2 circles
# we can get the radius by dividing the length by 4
radius = length/4
# convert plant distance to feet by dividing by 12
distance = distance/12

# the area of the garden is length squared
area_garden = length**2

# using the area of circle formula we get
# the area of the center circle and use that
# value to find the areas of the semi circles
area_center = pi*radius**2
area_edges = area_center/2

# the number of plants in each area can be found
# by squaring the distance between plants and dividing
# the area by this number, all values are converted to integers
plants_in_center = int(area_center//(distance**2))
plants_in_edge = int(area_edges//(distance**2))
plants_total = int((4*plants_in_edge)+plants_in_center)

# print results
print('\nSummary of needed plants:')
print('Each outer semi-circular bed:',plants_in_edge,'plants')
print('The center circular bed:',plants_in_center,'plants')
print('Total:',plants_total,'plants')

# all volume values were found using area*depth
# the total volume was calculated by adding the volume
# of 4 semi circles to 1 circle, all values rounded to 1 digit
volume_center = round((area_center*depth_flow)/27,1)
volume_edges = round(((area_edges*depth_flow))/27,1)
volume_total = round((4*volume_edges)+volume_center,1)

# print results
print('\nSummary of needed soil:')
print('Each outer semi-circular bed:',volume_edges,'cubic yards')
print('The center circular bed:',volume_center,'cubic yards')
print('Total:',volume_total)

# the area of fill is the total area minus the area
# of 3 full circles
area_fill = area_garden - (3*area_center)

# area*depth to get volume, divide by 27 to get cubic yards
# the resulting value is rounded
volume_fill = round((area_fill*depth_fill)/27,1)

# print results
print('\nSummary of your fill needs:')
print('Total:',volume_fill,'cubic yards')
