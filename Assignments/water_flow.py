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

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    '''
    Calculates the pressure loss due to fittings in a fluid flow system.

    Parameters:
        fluid_velocity (float): The velocity of the fluid (in meters per second).
        quantity_fittings (int): The number of fittings in the system.

    Returns:
        float: The pressure loss (in kilopascals) caused by the fittings.
    '''
    pressure_loss_fittings = (-0.04 * 998.2 * fluid_velocity ** 2 * quantity_fittings) / 2000
    return pressure_loss_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
    '''
    Calculates the Reynolds number for fluid flow in a pipe.

    Parameters:
        hydraulic_diameter (float): Hydraulic diameter of the pipe (meters).
        fluid_velocity (float): Velocity of the fluid (meters per second).

    Returns:
        float: Reynolds number.
    '''
    reynolds_number = (998.2 * hydraulic_diameter * fluid_velocity) / 0.0010016
    return reynolds_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    '''
    Calculates the pressure loss due to pipe reduction.

    Parameters:
        larger_diameter (float): Diameter of the larger pipe section (in meters).
        fluid_velocity (float): Velocity of the fluid in the pipe (in meters per second).
        reynolds_number (float): Reynolds number for the flow.
        smaller_diameter (float): Diameter of the smaller pipe section (in meters).

    Returns:
        float: Pressure loss (in kilopascals) due to pipe reduction.
    '''
    constant = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss_pipe_reduction = (-constant * 998.2 * fluid_velocity ** 2) / 2000
    return pressure_loss_pipe_reduction

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()