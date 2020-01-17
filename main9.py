from functools import reduce

def cook(food):
    if food == '🐄':
       return '🍔'
    elif food == '🥔':
       return '🍟'
    elif food == '🐔':
       return '🍗'
    elif food == '🌽':
       return '🍿'

def is_vegeterian(food):
    if food in ['🍿', '🍟']:
        return True
    return False


def eat(food1, food2):
    if food1 in ['🍔', '🍟', '🍗', '🍿', '💩']:
        return '💩'

if __name__=="__main__":
    cooked_foods = list(map(cook, ['🐄', '🥔', '🐔', '🌽']))
    print(cooked_foods)

    vegetrian_foods = list(filter(is_vegeterian, ['🍔', '🍟', '🍗', '🍿']))
    print(vegetrian_foods)

    result = reduce(eat,  ['🍔', '🍟', '🍗', '🍿'])
    print(result)

