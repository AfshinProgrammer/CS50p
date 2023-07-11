'''
Afshin Masoudi
CS50p/Problem Set 3/Felipe’s Taqueria
input : Taco, Baja Taco, Burger
'''
def taqueria(text= "Item: "):
    menu = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }

    total_cost = 0.00
    
    while True:
        try:
            input_str = input(text).strip().title()
            total_cost += menu[input_str]
        except EOFError:
            # exception EOFError
            # Raised when the input() function hits an end-of-file condition (EOF) 
            # without reading any data. (N.B.: the io.IOBase.read() and io.IOBase.readline() 
            # methods return an empty string when they hit EOF.)
            print()
            break
        except KeyError:
            # exception KeyError¶
            # Raised when a mapping (dictionary) key is not found in the set of existing keys.
            pass
        else:
            print(f"Total: ${total_cost:0.2f}")
    
def main():
    taqueria()
    
if __name__ == '__main__':
    main()