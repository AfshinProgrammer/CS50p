# Afshin Masoudi
# CS50p/Problem Set 4/Frank, Ian and Glen’s Letters
# input : CS50, Hello, world, Moo
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv_1 = ["-f", "--font"]

def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        figletize("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in argv_1 and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid usage")

def figletize(text, f):
    input_str = input(text).strip()
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(input_str))

if __name__ == "__main__":
    main()