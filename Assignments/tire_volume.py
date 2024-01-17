'''
01/10/2024
CSE 111-07
Nicholas Wilkins 

Calculating Tire Volume
'''

# to begin, import the math library so that pi can be used 
import math 

# next, set the variables and inputs 
tire_width = float(input('\nEnter the width of the tire as a whole number in mm (ex. 225): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex. 65): '))
wheel_diameter = float(input('Enter the diamter of the wheel in inches (ex. 17): '))

# now that all information has been gathered, complete the calculation
tire_volume = (math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * wheel_diameter)) / 10000000000

# print the result of the calculation
print(f'\nThe approximate volume is {tire_volume:.2f} liters.\n')