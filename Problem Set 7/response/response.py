# Afshin Masoudi
# CS50p/Problem Set 7/Response Validation
# input : malan@harvard.edu, malan@@@harvard.edu
import validators

def main():
    input_email = input("What's your email address? ").strip()
    if validators.email(input_email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()