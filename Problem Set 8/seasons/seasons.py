# Afshin Masoudi
# CS50p/Problem Set 8/Seasons of Love
# input : January 1, 1999, 1999-01-01, 1999-12-31, 1970-01-01
from datetime import date
import sys
import inflect

def get_date(input_date):
    try:
        return str(date.fromisoformat(input_date))
    except ValueError:
        return "Invalid date"

def convert_to_minutes(input_str):
    input = date.fromisoformat(input_str)
    now = date.today()
    days = str(now - input).split(' ')[0]
    return int(days) * 1440

def convert_to_words(input):
    pointer = inflect.engine()
    input_words = pointer.number_to_words(input)
    return input_words.replace(' and','').capitalize()

def main():
    date = get_date(input("Date of Birth: ").strip())
    if date == "Invalid date":
        sys.exit("Invalid date")
    minutes = convert_to_minutes(date)
    print(f"{convert_to_words(minutes)} minutes")

if __name__ == "__main__":
    main()