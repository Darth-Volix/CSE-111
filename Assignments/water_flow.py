'''
02/08/2024
CSE 111-07
Nicholas Wilkins 
Assignment 5:
Water Flow Calculator
'''
def water_column_height(tower_height, tank_height):
    '''
    Calculates the total water column height given a tower height and tank height.

    Parameters:
        tower_height (float): Height of the tower (in meters).
        tank_height (float): Height of the water tank (in meters).

    Returns:
        float: Total water column height (including tower and tank).
    '''
    column_height = tower_height + (3 * tank_height / 4)
    return column_height

def pressure_gain_from_water_height(height):
    '''
     Calculates the pressure gain due to water height.

    Parameters:
        height (float): Height of the water column (in meters).

    Returns:
        float: Pressure gain (in kilopascals, kPa).

    Formula:
        The pressure gain (P) due to water height (h) is given by:
        P = ρgh
        where:
        - ρ (rho) is the density of water (approximately 998.2 kg/m³).
        - g is the acceleration due to gravity (approximately 9.80665 m/s²).
    '''
    pressure_gain = (998.2 * 9.80665 * height / 1000)
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    '''
    Calculates pressure using the given formula:
    P = (-f * L * ρ * v**2) / (2000 * d)

    Parameters:
        f (float): Friction factor.
        L (float): Length of the pipe or channel (in meters).
        ρ (float): Density of the fluid (in kg/m³).
        v (float): Velocity of the fluid (in m/s).
        d (float): Diameter of the pipe or channel (in meters).

    Returns:
        float: Pressure (in pascals).
    '''
    pressure_loss = (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure_loss