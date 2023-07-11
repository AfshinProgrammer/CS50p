# Afshin Masoudi
# CS50p/Problem Set 6/CS50 P-Shirt
# cmd : python shirt.py, python shirt.py before1.jpg before2.jpg before3.jpg, python shirt.py before1.jpg invalid_format.bmp,
# python shirt.py before1.jpg after1.png, python shirt.py non_existent_image.jpg after1.jpg, python shirt.py before1.jpg after1.jpg
import sys
import os
from PIL import Image, ImageOps

def get_filenames():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        form = [".jpg", ".jpeg", ".png"]
        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        if output[1].lower() not in form:
            sys.exit("Invalid output")
        elif input[1].lower() != output[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            return [sys.argv[1], sys.argv[2]]

def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

def main():
    filenames = get_filenames()
    edit_photo(filenames[0], filenames[1])

if __name__ == "__main__":
    main()