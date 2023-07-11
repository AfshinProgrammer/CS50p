'''
Afshin Masoudi
CS50p/Problem Set 1/Math Interpreter
input : '1 + 1', '2 - 3', '2 * 2', '50 / 5'
'''

def interpreter(x, y, z):
    num_1 = float(x)
    num_2 = float(z)
    result = -1.0
    if y == '+':
        result = num_1 + num_2
    elif y == '-': 
        result = num_1 - num_2
    elif y == '*': 
        result = num_1 * num_2
    elif y == '/': 
        result = num_1 / num_2
    elif y == '%': 
        result = num_1 % num_2
    elif y == '^': 
        result = num_1 ** num_2
    else:
        print(">> Error happened ... :(")
    print(f"{result:0.1f}")

def main():
    expression = input("Please enter an arithmetic expression in " + 
                   "the form of x y z : ").strip()
    x, y, z = expression.split(' ')
    interpreter(x, y, z)

if __name__ == '__main__':
    main()
