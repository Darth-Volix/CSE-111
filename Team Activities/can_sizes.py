'''
Team Activity (Week 4): Can Size Efficiency
CSE 111-07
Nicholas Wilkins 
01/31/2024
'''
# import math library for use later 
import math 

# set up the initial lists
can_name = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z Short', '#10', '#211', '#300', '#303']
can_radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
can_cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

# set up lists for data used in calculations and output 
can_volume = []
can_surface_area = []
can_storage_efficiency = []

def compute_volume(radius, height):
    # compute the volume of the can given the radius and the height of the can
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    # compute the surface area of the can given the radius and the height
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    # compute the storage efficiency of the can given volume and surface area
    storage_efficiency = volume / surface_area 
    return storage_efficiency

def main():
    # main function of the program

    # start by computing the can volume, surface area, and storage efficiency for each can
    for i in range(len(can_name)):
        radius = can_radius[i]
        height = can_height[i]
        volume = compute_volume(radius, height)
        can_volume.append(volume)
        surface_area = compute_surface_area(radius, height)
        can_surface_area.append(surface_area) 
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        can_storage_efficiency.append(storage_efficiency)
    
    # print the output of the storage efficency calculation
    for i in range(len(can_name)):
        print(f'{can_name[i]}: {can_storage_efficiency[i]:.2f}')

# call the main function of the program
main()