spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

get_names(spicy_foods)
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if (food['heat_level'] > 5)]

def print_spicy_foods(spicy_foods):
    spicy = []
    for food in spicy_foods:
        spicy.append(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}")
    print('\n'.join(spicy))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food['cuisine']:
            return food
        
            
        

def print_spiciest_foods(spicy_foods):
    spicy_food_list = []
    for food in spicy_foods:
        if food['heat_level'] > 5:
            spicy_food_list.append(f"{food['name']} ({food['cuisine']}) | Heat Level: {food['heat_level'] * '🌶'}")
    for spicy_food in spicy_food_list:
        print(spicy_food)
    
    
      

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

   
