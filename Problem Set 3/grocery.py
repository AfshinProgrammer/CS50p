'''
Afshin Masoudi
CS50p/Problem Set 3/Grocery List
input : mango, strawberry or milk, milk and tortilla, sweet potato
'''
def grocery_list():
    grocery_dic = {}

    while True:
        try:
            input_str = input().strip().title()
            if input_str in grocery_dic:
                # Update item's quantity
                grocery_dic[input_str] += 1
            else:
                # Initialize item's quantity in grocery
                grocery_dic[input_str] = 1
            # ctrl+d or ctrl+z >> make EOFError 
        except EOFError:
            # Sort item's quantity
            sorted_grocery_dic = dict(sorted(list(grocery_dic.items())))
            # Print items' sorted quantity
            for item in sorted_grocery_dic:
                print(sorted_grocery_dic[item], item.upper(), sep=" ")

            break
        except KeyError:
            pass
        except ValueError:
            pass

    return sorted_grocery_dic

def main():
    grocery_list()

if __name__ == '__main__':
    main()