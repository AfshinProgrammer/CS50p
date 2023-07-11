'''
Afshin Masoudi
CS50p/Problem Set 5/Back to the Bank
cmd : pytest test_bank.py
'''
from bank import value

def test_value():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100