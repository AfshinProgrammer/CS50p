# Afshin Masoudi
# CS50p/Problem Set 4/Bitcoin Price Index
# input : python bitcoin.py 1, python bitcoin.py 2, python bitcoin.py 2.5
import requests
import sys

def get_btc_price(num_bitcoins):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]
        cost = num_bitcoins * price
        return f"${cost:,.4f}"
    except requests.RequestException:
        return None

def main():
    if len(sys.argv) == 2:
        try:
            number_bitcoins = float(sys.argv[1])
            print(get_btc_price(number_bitcoins))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()