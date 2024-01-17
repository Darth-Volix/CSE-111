'''
Checkpoint 2: Calling Functions
CSE 111-07
Nicholas Wilkins
01/14/2023
'''

# import the math library in order to use math functions 
import math 

# have the user input the number of items and the number of items per box
number_of_items = int(input('\nEnter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

# calculate the number of boxes needed 
boxes = math.ceil((number_of_items / items_per_box))

# output the result 
print(f'\nFor {number_of_items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.\n')