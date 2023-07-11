# Afshin Masoudi
# CS50p/Problem Set 7/Regular, um, Expressions
import pytest
from um import count

def test_input():
    assert count("Um, thanks for the album.") == 1
    assert count("um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1