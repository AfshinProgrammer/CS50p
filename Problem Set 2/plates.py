'''
Afshin Masoudi
CS50p/Problem Set 2/Vanity Plates
input : CS50 , CS05 , CS50P, PI3.14, H, OUTATIME, CS50P2  
'''

def is_valid(input):
    if 2 <= len(input) <= 6 and input.isalnum():
        # Return true if characters are all letters
        if input.isalpha(): 
            return True
        else:
            # Check for number in the middle 
            # (only if the first two characters are letters and the last character is number)
            if input[:2].isalpha() and input[-2:].isdigit():
                for i in range(len(input)):
                    if input[i].isdigit():
                        # Return false if number starts with 0 or the following character is letter
                        if input[i].startswith("0") or input[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False

def main():
    input_str = input("Plate: ").strip()
    if is_valid(input_str):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()