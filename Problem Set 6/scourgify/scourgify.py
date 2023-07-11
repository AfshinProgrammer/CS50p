# Afshin Masoudi
# CS50p/Problem Set 6/Scourgify
# cmd : python scourgify.py, python scourgify.py 1.csv 2.csv 3.csv, python scourgify.py invalid_file.csv output.csv,
# python scourgify.py before.csv after.csv
import csv
import sys

def input_to_output(input_filename, output_filename):
    try:
        with open(input_filename) as input_csvfile:
            reader = csv.DictReader(input_csvfile)
            with open(output_filename, "w") as output_csvfile:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output_csvfile, fieldnames = header)
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_filename}")

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            input_to_output(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()