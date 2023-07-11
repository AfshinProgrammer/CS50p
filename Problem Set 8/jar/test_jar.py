# Afshin Masoudi
# CS50p/Problem Set 8/Cookie Jar
# cmd : pytest test_jar.py
from jar import Jar
import pytest
# cd Object_Oriantation
# pytest test_jar.py

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar("20")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(20)
    with pytest.raises(ValueError):
        jar.deposit("20")

def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(20)
    with pytest.raises(ValueError):
        jar.withdraw("20")