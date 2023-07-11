# Control Error
# SyntaxError >> in command lines
# x = int(input('What\'s X : )) >> SyntaxError

# ValueError >> in the result of codes
# x = int(input('What\'s X : ')) >> input 'cat'>> ValueError

# nameError >> when you use undefined variables
# x = int(input('What\'s X : ')) 
# print(f'X is {digit}.')>> use digit>> nameError

# use it to control errors
# try: بلوکی که احتمال بروز خطا داریم
#    ...
# except <Errors>:  زمانی اجرا می شد که خطا از نوع مشخص شده داشته باشیم
#   ... 
# else: # زمانی اجرا می شه که خطا نداشته باشیم
#   ...
# finally:
#   ...
import os
from time import sleep

def input_int(text, min, max):
    while True:
        os.system('cls')
        try:
            output = int(input(text).strip())
        except ValueError:
            print('Input is NOT an Integer ...!')
        else:
            if min <= output <= max:
                return output 
            else:
                print(f'Input is out of range ({min} - {max}).')
                
        sleep(1)
    
def input_int(text):
    while True:
        os.system('cls')
        try:
            return int(input(text).strip())
        except ValueError:
            print('Input is NOT an Integer ...!')
                
        sleep(1) 
            
def main():
    x = input_int('Enter a number : ')
    print(f'X is {x}.')
    # print(f'X is {digit}.')>> use digit>> nameError

if __name__ == '__main__':
    main()



