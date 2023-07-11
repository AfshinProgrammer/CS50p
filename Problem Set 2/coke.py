'''
Afshin Masoudi
CS50p/Problem Set 2/Coke Machine
input : Insert Coin : 25, 10, 5, 30, 25, ..
'''
def accept_coin(coin):
    coins = [5, 10, 25]
    if coin in coins:
        return coin
    else:
        return 0
     
def main():
    amount_due = 50
    amount_inserted = 0
    
    while True:
        coin = int(input("Insert Coin: ").strip())
        coin_value = accept_coin(coin)
        amount_inserted += coin_value
        
        if amount_inserted < amount_due:
            print(f"Amount Due: {amount_due - amount_inserted}")
        else:
            print(f"Change Owed: {amount_inserted - amount_due}")
            break
        
if __name__ == "__main__":
    main()