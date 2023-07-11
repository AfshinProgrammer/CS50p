# Afshin Masoudi
# CS50p/Problem Set 4/Guessing Game
# input : 1, 10, cat, -1
from random import randint

def get_level(text="Level: "):
    while True:
        try:
            level = int(input(text).strip())
            if level < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    return level

def get_guess(text="Guess: "):
    while True:
        try:
            guess = int(input(text).strip())
            if guess < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            break

    return guess

def game():
    level = get_level()
    number = randint(1, level)
    while True:
        guess = get_guess()

        if guess < number:
            print('Too small!')
        elif guess > number:
            print('Too large!')
        else:
            print('Just right!')
            break

def main():
    game()

if __name__ == "__main__":
    main()