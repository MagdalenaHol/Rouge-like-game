# items
def create_shovel():
    shovel = {
        'name': 'Shovel',
        'type': "Key",
        'amount': 1,
        'pos_x': 5,
        'pos_y': 5,
        'icon': 'X',
        "usable": "no"
    }
    return shovel


def create_potion(x, y):
    potion = {
        'name': 'Potion',
        'amount': 3,
        'healing': 30,
        'pos_x': x,
        'pos_y': y,
        'icon': 'P',
        "usable": "yes"
    }
    return potion


def create_mushroom(x, y):
    mushroomn = {
        'name': 'Mushroom',
        'amount': 3,
        'healing': 30,
        'pos_x': x,
        'pos_y': y,
        'icon': 'M',
        "usable": "yes"
    }
    return mushroomn


def create_stick():

    stick = {
        'name': 'Stick',
        'type': 'weapon',
        'amount': 1,
        'damage': 30,
        "usable": "no",
        'pos_x': 7,
        'pos_y': 7,
        'icon': 'T',
    }
    return stick

    # enemies


def create_enemy_1():
    enemy_1 = {
        'name': "Snake",
        'is_alive': True,
        'health': 35,
        'damage': 20,
        'pos_x': 10,
        'pos_y': 10,
        'icon': '§',
    }
    return enemy_1


def create_enemy_2():
    enemy_2 = {
        'name': "Boar",
        'is_alive': True,
        'health': 70,
        'damage': 40,
        'pos_x': 18,
        'pos_y': 5,
        'icon': '¤',
    }
    return enemy_2


def create_enemy_3():
    enemy_3 = {
        'name': "Mosquito",
        'is_alive': True,
        'health': 1,
        'damage': 99,
        'pos_x': 17,
        'pos_y': 26,
        'icon': ',',
    }
    return enemy_3


def create_boss():
    boss = {
        'name': "Boss",
        'is_alive': True,
        'health': 199,
        'damage': 7,
        'pos_x': 10,
        'pos_y': 10,
        'icon': 'B',
    }
    return boss
