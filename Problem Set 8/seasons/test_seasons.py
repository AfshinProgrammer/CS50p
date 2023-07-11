# Afshin Masoudi
# CS50p/Problem Set 8/Seasons of Love
# cmd : pytest test_seasons.py
import pytest
from seasons import get_date, convert_to_minutes ,convert_to_words

def test_get_date_input():
    assert get_date("January 1, 1999") == 'Invalid date'
    assert get_date("2012-13-12") == 'Invalid date'
    assert get_date("2012-12-32") == 'Invalid date'
    assert get_date("2012-32-12") == 'Invalid date'
    assert get_date("12-12-12") == 'Invalid date'
    assert get_date("2012-322-12") == 'Invalid date'
    assert get_date("323-1-1") == 'Invalid date'


def test_convert_to_minutes():
    assert convert_to_minutes("1999-01-01") == 12811680
    assert convert_to_minutes("1999-12-31") == 12287520
    assert convert_to_minutes("1970-01-01") == 28064160

def test_convert_to_words():
    assert convert_to_words(12811680) == "Twelve million, eight hundred eleven thousand, six hundred eighty"
    assert convert_to_words(12287520) == "Twelve million, two hundred eighty-seven thousand, five hundred twenty"
    assert convert_to_words(28064160) == "Twenty-eight million, sixty-four thousand, one hundred sixty"