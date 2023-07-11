'''
Afshin Masoudi
CS50p/Problem Set 1/Meal Time
input : '7:00', '7:30', '12:42', '18:32', '11:11',
        '7:30 a.m.', '12:42 p.m.', '6:32 p.m.', '0:45 a.m.'
'''

def convert(time):
    hours, minutes = time.split(':')
    if 'a.m.' in minutes:
        min, s = minutes.split(' ')
        output = float(hours) + float(min) / 60
    elif 'p.m.' in minutes:
        min, s = minutes.split(' ')
        output = float(hours) + 12.0 + float(min) / 60
    else:
        hours, minutes = time.split(':')
        output = float(hours) + float(minutes) / 60
    return output

def meal_time(time):
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        pass  # don't output anything

def main():
    time_str = input("Enter a time in 24-hour format (##:##) or 12-hour format (##:## a.m. and ##:## p.m.): ").strip()
    time = convert(time_str)
    meal_time(time)
    
if __name__ == "__main__":
    main()