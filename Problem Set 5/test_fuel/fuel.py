'''
Afshin Masoudi
CS50p/Problem Set 5/Refueling
'''
def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(frac):
    x, y = frac.split("/")
    if int(x)/int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return int(int(x)/int(y) * 100)

def gauge(perc):
    try:
        if 0 <= perc <= 1:
            return "E"
        elif 99 <= perc <= 100:
            return "F"
        elif 1 < perc < 99:
            return f"{int(perc)}%"
        else:
            raise TypeError
    except TypeError:
        pass

if __name__ == "__main__":
    main()