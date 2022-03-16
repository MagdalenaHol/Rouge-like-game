import util
import sys
import engine

def create_board(width, height):
    board = []
    for i in range(height):
        board.append([' '] * width)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 or i == len(board)-1:
                board[i][j] = "_"
            else:
                board[i][j] = " "
            if j == 0 or j == len(board[i])-1:
                board[i][j] = "|"

    board[0][0] = "."
    board[0][29] = "."
    board[19][0] = "."
    board[19][29] = "."
    return board


def put_player_on_board(board, player):
    board[player['pos_x']][player['pos_y']] = player['icon']
    '''
    Modifies the game board by placing the player icon at its coordinates.
    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates
    Returns:
    Nothing
    '''

    return player



def movement_phase(player, key, board):
    obstacles = ['|', '_']
    while True:
        if key == 'w':
            if board[player['pos_x'] - 1][player['pos_y']] in obstacles:
                break
            else:
                player['pos_x'] = player['pos_x'] - 1
                break
        elif key == 's':
            if board[player['pos_x'] + 1][player['pos_y']] in obstacles:
                break
            else:
                player['pos_x'] = player['pos_x'] + 1
                break
        elif key == 'a':
            if board[player['pos_x'] ][player['pos_y'] - 1] in obstacles:
                break
            else:
                player['pos_y'] = player['pos_y'] - 1    
                break    
        elif key == 'd':
            if board[player['pos_x'] ][player['pos_y'] + 1] in obstacles:
                break
            else:
                player['pos_y'] = player['pos_y'] + 1 
                break        
        else:
            key = util.key_pressed()
            if key == 'q':
                sys.exit()



def put_enemy_on_board(board):
    enemy = create_enemy()
    board[enemy['pos_x']][enemy['pos_y']] = enemy['icon']


def put_items_on_board(board,items):
    #items[0]-key
    #items[1]-stick
    #items[2]-potion1
    
    board[items[0]['pos_x']][items[0]['pos_y']] = items[0]['icon']
    board[items[1]['pos_x']][items[1]['pos_y']] = items[1]['icon']
    board[items[2]['pos_x']][items[2]['pos_y']] = items[2]['icon']
    
def add_to_inventory(player,item):
    item.pop('pos_y', None)
    item.pop('pos_x', None)
    item.pop('icon', None)
    if item["name"] not in player.keys():
        player['inventory'] [item["name"]] =item
    else:
        player['inventory'] [item["amount"]] += [item["amount"]]
        pass    
    return player



def events(player, board,item):
    if board[player['pos_x']][player['pos_y']] == 'X':
        board[item[0]['pos_x']][item[0]['pos_y']] == ' '
        add_to_inventory(player,item[0])
        print('Zdobywasz klucz!')
    #miksturki to itemy     
    if board[player['pos_x']][player['pos_y']] == 'T':
        board[item[1]['pos_x']][item[1]['pos_y']] == ' '
        add_to_inventory(player,item[1])
        print('Zdobywasz miecz!')
    if board[player['pos_x']][player['pos_y']] == 'P':
        board[item[2]['pos_x']][item[2]['pos_y']] == ' '
        add_to_inventory(player,item[2])
        print('Zdobywasz miksturki!')
#    if board[player['pos_x']][player['pos_y']] == 'P':
#        board[item[3]['pos_x']][item[3]['pos_y']] == ' '
#        add_to_inventory(player,item[3])
#        print('Zdobywasz miksturki!')
    if board[player['pos_x']][player['pos_y']] == '§':
        util.clear_screen()
       # battle.new_battle(player, enemy())

##########################
def create_enemy():    
    enemy_1 = {
        'name': "Snake",
        'health': 15,
        'damage': 30,
        'pos_x': 5,
        'pos_y': 18,
        'icon' : '§',
        }
    return enemy_1


player = {
        'name': "Player",
        'health': 100,
        'damage': 30,
        'inventory': {
                'mushroom': 1,
                'torch': 22    
        }
    }

def create_items():
    key = create_key()
    stick = create_stick()
    potion1 = create_potion(13,13)
    potion2 = create_potion(13,4)
    return key , stick, potion1 


def create_key():
    key ={
        'name' : 'Key',
        'amount' : 1,
        'pos_x': 5,
        'pos_y': 5,
        'icon' : 'X',
    }
    return key
def create_potion(x,y):
    potion = {
    'name': 'potion',
    'amount' : 3,
    'damage': 30,
    'pos_x': x,
    'pos_y': y,
    'icon': 'P',
    }
    return potion

def create_stick():
      
    stick = {
        'name' : 'stick',
        'type' : 'weapon',
        'amount' : 1,
        'damage': 30,
        'pos_x': 7,
        'pos_y': 7,
        'icon' : 'T',
    }
    return stick


