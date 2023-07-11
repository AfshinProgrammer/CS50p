# Afshin Masoudi
# CS50p/Problem Set 7/NUMB3RS
# cmd : pytest test_numb3rs.py
from numb3rs import validate
import pytest

def test_validate():
    # Test valid IP addresses
    assert validate('192.168.0.1') == True
    assert validate('10.0.0.1') == True
    assert validate('172.16.0.1') == True
    assert validate('255.255.255.255') == True

    # Test invalid IP addresses
    assert validate('192.168.0') == False
    assert validate('10.0.0.256') == False
    assert validate('172.16.0.0.1') == False
    assert validate('foo.bar.baz.qux') == False