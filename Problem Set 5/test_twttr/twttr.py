'''
Afshin Masoudi
CS50p/Problem Set 5/Just setting up my twttr
input : Twitter, What's your name?, CS50
'''

def main():
    input_str = input("Input: ").strip()
    print(f"Output: {shorten(input_str)}" )

def shorten(word):
    vowels = "aAeEiIoOuU"
    output = ""

    for char in word:
        if char not in vowels:
            output += char

    return output

if __name__ == "__main__":
    main()