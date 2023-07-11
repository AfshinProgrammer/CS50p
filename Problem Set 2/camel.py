'''
Afshin Masoudi
CS50p/Problem Set 2/camelCase
input : name, firstName, preferredFirstName 
'''
def camelCase(input):
    output = ""
    for i, char in enumerate(input):
        if char.isupper() and i != 0:
            output += "_"
        output += char.lower()
    return output 

def main():
    output_str = input("Enter a name in camel case : ")
    print(f"The snake case version of the name is : {camelCase(output_str)}")

if __name__ == '__main__':
    main()

