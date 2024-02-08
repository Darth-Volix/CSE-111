'''
02/08/2024
CSE 111-07
Nicholas Wilkins 
Assignment 5:
Testing the Water Flow Calculator
'''
from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
import pytest

def test_water_column_height():
    '''
    Test function for the water_column_height function.
    This function checks various scenarios by asserting expected results. 
    '''
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    '''
    Test function for the pressure_gain_from_water_height function.
    This function checks various scenarios by asserting expected results.
    '''
    assert pressure_gain_from_water_height(0) == approx(0, abs = 0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs = 0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs = 0.001)

def test_pressure_loss_from_pipe():
    '''
    Test function for the pressure_loss_from_pipe function. 
    This function checks various scenarios by asserting expected results.
    '''
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs = 0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs = 0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs = 0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs = 0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])