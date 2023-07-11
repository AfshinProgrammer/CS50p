# Afshin Masoudi
# CS50p/Problem Set 4/Adieu, Adieu
# input : 'Liesl', 'Frie','drich', 'Louisa', 'Kurt', 'Brigitta', 'Marta', 'Gretl'
import inflect


def adieu(text="Name: "):
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input(text).strip().title()
            names.append(name)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}")
            break

def main():
    adieu()

if __name__ == "__main__":
    main()