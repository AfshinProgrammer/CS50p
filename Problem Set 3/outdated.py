'''
Afshin Masoudi
CS50p/Problem Set 3/Outdated
input : 9/8/1636, September 8, 1636, 23/6/1912, December 80, 1980
'''
def outdated(text= "Date: "):
    months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]

    while True:
        try:
            date_str = input(text).strip()

            if "/" in date_str:
                month, day, year = date_str.split("/")
                month = int(month); day = int(day); year = int(year)
            elif "," in date_str:
                month_day, year = date_str.split(", ")
                month, day = month_day.split(" ")
                month = int(months.index(month.title())) + 1
                day = int(day); year = int(year)
            else:
                raise ValueError
                
            if month > 12 or day > 31:
                raise ValueError
        except (AttributeError, ValueError, NameError, KeyError):
            pass
        else:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    return [year, month, day]

def main():
    outdated()

if __name__ == '__main__':
    main()