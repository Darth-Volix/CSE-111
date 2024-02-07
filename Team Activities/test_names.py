'''
02/07/2024
CSE 111-07
Nicholas Wilkins 
Team Activity 5: Testing names.py Functions
'''
from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    ''' Test to make sure that the make_full_name function returns a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".
    '''
    assert make_full_name('Nick', 'Wilkins') == 'Wilkins; Nick'
    assert make_full_name('Jannetta', 'Stephens') == 'Stephens; Jannetta'
    assert make_full_name('Jose', 'Ricardo-Richardson') == 'Ricardo-Richardson; Jose'
    assert make_full_name('Sam', 'Smith') == 'Smith; Sam'

def test_extract_family_name():
    ''' Test to make sure that the function extracts and returns the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".
    '''
    assert extract_family_name('Wilkins; Nick') == 'Wilkins'
    assert extract_family_name('Stephens; Jannetta') == 'Stephens'
    assert extract_family_name('Ricardo-Richardson; Jose') == 'Ricardo-Richardson'
    assert extract_family_name('Smith; Sam') == 'Smith'

def test_extract_given_name():
    ''' Test to make sure that the function extracts and returns the given name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".
    '''
    assert extract_given_name('Wilkins; Nick') == 'Nick'
    assert extract_given_name('Stephens; Jannetta') == 'Jannetta'
    assert extract_given_name('Ricardo-Richardson; Jose') == 'Jose'
    assert extract_given_name('Smith; Sam') == 'Sam'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])