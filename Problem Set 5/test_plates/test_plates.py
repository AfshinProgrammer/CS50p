'''
Afshin Masoudi
CS50p/Problem Set 5/Re-requesting a Vanity Plate
cmd : pytest test_plates.py
'''
from plates import is_valid

def test_begin_two_letters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False

def test_length():
    assert is_valid("HICS50") == True
    assert is_valid("CS") == True
    assert is_valid("HELLOCS50") == False

def test_number():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punct():
    assert is_valid("CS50!") == False