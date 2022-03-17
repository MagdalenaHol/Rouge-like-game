                                            #### items
def create_shovel():
    shovel = {
        'name': 'Shovel',
        'amount': 1,
        'pos_x': 5,
        'pos_y': 5,
        'icon': 'X',
    }
    return shovel


def create_potion(x, y):
    potion = {
        'name': 'potion',
        'amount': 3,
        'healing': 30,
        'pos_x': x,
        'pos_y': y,
        'icon': 'P',
    }
    return potion


def create_stick():

    stick = {
        'name': 'stick',
        'type': 'weapon',
        'amount': 1,
        'damage': 30,
        'pos_x': 7,
        'pos_y': 7,
        'icon': 'T',
    }
    return stick


                                                    ###############   enemies    
def create_enemy_1():
    enemy_1 = {
        'name': "Snake",
        'health': 35,
        'damage': 20,
        'pos_x': 5,
        'pos_y': 18,
        'icon': '§',
    }
    return enemy_1


def create_enemy_2():    
    enemy_2 = {
        'name': "Boar",
        'health': 70,
        'damage': 40,
        'pos_x': 18,
        'pos_y': 5,
        'icon' : '¤',
        }
    return enemy_2

def create_enemy_3():    
    enemy_3 = {
        'name': "Mosquito",
        'health': 1,
        'damage': 99,
        'pos_x': 17,
        'pos_y': 26,
        'icon' : ',',
        }
    return enemy_3