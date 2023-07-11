'''
Afshin Masoudi
CS50p/Problem Set 5/Re-requesting a Vanity Plate
'''
def main():
    input_str = input("Plate: ").strip()
    
    if is_valid(input_str):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i].startswith("0") or s[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()