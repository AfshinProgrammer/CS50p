# Afshin Masoudi
# CS50p/Problem Set 4/Emojize
# input : :1st_place_medal:, :money_bag:, :smile_cat:
import emoji as ej

def emojize():
    input_str = input("Enter a string in English: ").strip()
    emojized_str = ej.emojize(input_str)

    print(f"Output: {emojized_str}")

def main():
    emojize()

if __name__ == "__main__":
    main()