# Afshin Masoudi
# CS50p/Problem Set 6/Scourgify
# cmd : python scourgify.py, python scourgify.py 1.csv 2.csv 3.csv, python scourgify.py invalid_file.csv output.csv,
# python scourgify.py before.csv after.csv
import csv
import sys

# Check command-line arguments
def get_filenames():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        filenames = sys.argv[1:]

        if len(filenames) < 2:
            filenames.append("after.csv")

        if not (filenames[0].lower().endswith(".csv") and filenames[1].lower().endswith(".csv")) :
            sys.exit("Not a CSV file")
        elif filenames[0].lower() != "before.csv":
            sys.exit(f"Could not read {filenames[0]}")
        else:
            return filenames

def clear_data(input_filename, output_filename):
    try:
        # Open input and output files
        with open(input_filename, "r") as input_csvfile:
            with open(output_filename, "w") as output_csvfile:
                # Set up CSV readers and writers
                reader = csv.DictReader(input_csvfile, fieldnames=["name", "house"])
                writer = csv.DictWriter(output_csvfile, fieldnames = ["first", "last", "house"])
                # Write header to output file
                writer.writeheader()
                # Create a list for output
                output = []
                # Process each row of input file
                for student in reader:
                    # Split name into first and last
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    # Creat a row of output data
                    row_dict = {"first": first, "last": last, "house": house}
                    # Write row to output file
                    writer.writerow(row_dict)
                    output.append(row_dict)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except PermissionError:
        sys.exit(f"Permission denied to output {output_filename}")
    else:
        return output

def main():
    filename = get_filenames()
    clear_data(filename[0], filename[1])

if __name__ == "__main__":
    main()
