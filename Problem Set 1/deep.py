'''
Afshin Masoudi
CS50p/Problem Set 1/Deep Thought
input : '42', 'Forty Two', 'forty-two'
'''

def output(answer):
    answers = ['42', 'forty two', 'forty-two']

    if answer == '42' or answer == 'forty two' or answer == 'forty-two':
        print("Yes")
    else:
        print("No")

def main():
    input_answer = input().strip().lower()
    output(input_answer)

if __name__ == '__main__':
    main()