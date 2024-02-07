'''
02/07/2024
CSE 111-07
Nicholas Wilkins 
Team Activity 5 Stretch: Testing address.py Functions
'''
from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    ''' Test function to ensure that it extractst and returns the name of a city from
    a properly formatted U.S. mailing address.
    '''
    assert extract_city('1142 W Wasatch Downs Drive, South Jordan, UT 84095') == 'South Jordan'
    assert extract_city('940 S 5th W, Rexburg, ID 83440') == 'Rexburg'
    assert extract_city('70 S 300 E, Orem, UT 84058') == 'Orem'

def test_extract_state():
    ''' Test function to ensure that it extractst and returns the name of a State from
    a properly formatted U.S. mailing address.
    '''
    assert extract_state('1142 W Wasatch Downs Drive, South Jordan, UT 84095') == 'UT'
    assert extract_state('940 S 5th W, Rexburg, ID 83440') == 'ID'
    assert extract_state('70 S 300 E, Orem, UT 84058') == 'UT'

def test_extract_zipcode():
    ''' Test function to ensure that it extractst and returns the zipcode from
    a properly formatted U.S. mailing address.
    '''
    assert extract_zipcode('1142 W Wasatch Downs Drive, South Jordan, UT 84095') == '84095'
    assert extract_zipcode('940 S 5th W, Rexburg, ID 83440') == '83440'
    assert extract_zipcode('70 S 300 E, Orem, UT 84058') == '84058'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])