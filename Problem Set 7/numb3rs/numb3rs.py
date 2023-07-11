# Afshin Masoudi
# CS50p/Problem Set 7/NUMB3RS
# input : 127.0.0.1, 255.255.255.255, 512.512.512.512, 1.2.3.1000, cat
import re

def validate(ip4):
    pattern = "^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    if match := re.search(pattern, ip4):
        numbers = [int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))]
        if (0 <= numbers[0] <= 255) and (0 <= numbers[1] <= 255) and (0 <= numbers[2] <= 255) and (0 <= numbers[3] <= 255):
            return True

    return False

def main():
    print(validate(input("IPv4 Address: ").strip()))

if __name__ == "__main__":
    main()