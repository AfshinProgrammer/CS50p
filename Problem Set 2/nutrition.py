'''
Afshin Masoudi
CS50p/Problem Set 2/Nutrition Facts
input : Apple , Avocado , Sweet Cherries  
'''

def nutrition_facts(fruit):
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }
    
    if fruit in fruits:
        print(f'Calories: {fruits[fruit]}')
    else:
        print("Invalid fruit.")
    
def main():
    fruit = input("Enter a fruit: ").strip().title()
    nutrition_facts(fruit)
    
if __name__ == "__main__":
    main()