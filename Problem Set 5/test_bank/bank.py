'''
Afshin Masoudi
CS50p/Problem Set 5/Back to the Bank
'''

def main():
    input_str = (input("Greeting: ")).strip().lower()
    print(f"${value(input_str)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()