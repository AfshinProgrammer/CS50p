# Afshin Masoudi
# CS50p/Problem Set 7/Working 9 to 5
# input :
import re

def main():
    print(convert(input("Hours: ")))

def convert(input):
    regex = "^(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)$"
    if match := re.search(regex, input):
        from_time = Set_time(match.group(1), match.group(2), match.group(3))
        to_time = Set_time(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {to_time}"
    else:
        raise ValueError

def Set_time(hr, min, x):
    if hr != "12":
        if x == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr) + 12:02}"
    else:
        if x == "AM":
            hour = "00"
        else:
            hour = "12"

    if min == None:
        minute = "00"
    else:
        minute = f"{int(min):02}"

    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()