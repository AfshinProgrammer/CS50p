# Afshin Masoudi
# CS50p/Problem Set 7/Regular, um, Expressions
# input : um, um?, Um, thanks for the album., Um, thanks, um...,
import re

def main():
    print(count(input("Text: ")))

def count(text):
    count = 0
    words = re.findall(r'\b\w*um\w*\b', text, re.IGNORECASE)
    for word in words:
        if word.lower() == 'um':
            count += 1
    return count

if __name__ == "__main__":
    main()