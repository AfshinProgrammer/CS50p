# Afshin Masoudi
# CS50p/Problem Set 4/Little Professor
# input : -1, 4, 1
from random import randint

def main():
    eqn = 10
    score = 0
    chances = 3
    level = get_level()

    while eqn != 0:
        if chances == 3: # User have 3 chances to answer each equation
            # Only generate_integer for new equation if chances == 3
            x, y = generate_integer(level)
        try:
            input_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if input_answer == answer:
                eqn = eqn - 1
                score = score + 1
                chances = 3 # Reset chances to generate new equation in case user input the right answer on 2nd/3rd try
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass

        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3 # Reset chances to generate new equation
            eqn = eqn - 1
            continue

    print(f"Score: {score}")

def get_level(text="Level: "):
    while True:
        try:
            level = int(input(text).strip())
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass

    return level

def generate_integer(level):
    max_number = (10 ** level) - 1
    min_number = 10 ** (level - 1)

    if level == 1:
        min_number = 10 ** (level - 1) - 1
    else:
        min_number = 10 ** (level - 1)

    x = randint(min_number, max_number)
    y = randint(min_number, max_number)

    return x, y

if __name__ == "__main__":
    main()