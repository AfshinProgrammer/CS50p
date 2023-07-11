'''
Afshin Masoudi
CS50p/Problem Set 1/Home Federal Savings Bank
input : 'Hello', 'Hello, Newman', 'How you doing?', 'What's happening?'
'''

def answer(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

def main():
    input_str = input("Please enter your greeting: ").strip().lower()
    answer(input_str)

if __name__ == '__main__':
    main()