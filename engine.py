import util
import sys
import random
import battle
import engine
import creating_things


def get_file_board(file_name):
    file = open(file_name, "r")
    board = file.readlines()
    return board


def create_board(file_name):
    board = get_file_board(file_name)
    split_board = []
    for line in board:
        split_lines = list(line)
        split_lines = split_lines[:-1]
        split_board.append(split_lines)
    return split_board


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
            if board[player['pos_x']][player['pos_y'] - 1] in obstacles:
                break
            else:
                player['pos_y'] = player['pos_y'] - 1
                break
        elif key == 'd':
            if board[player['pos_x']][player['pos_y'] + 1] in obstacles:
                break
            else:
                player['pos_y'] = player['pos_y'] + 1
                break
        else:
            key = util.key_pressed()
            if key == 'q':
                sys.exit()

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

def put_enemy_on_board(enemy, board):
    board[enemy['pos_x']][enemy['pos_y']] = enemy['icon']




def is_position_a_border(board, coordinates):
    coordinates_on_board = board[coordinates[0]][coordinates[1]]
    return coordinates_on_board == ['|'] or coordinates_on_board == ['-'] 


def enemy_direction_move(enemy_X, enemy_Y, board):
    proper_directions = ["w", "s", "a", "d"]
    # direction_list = ((-1, 0), (1, 0), (0, 1), (0, -1))
    direction_list = [-1,1]
    enemy_position = [enemy_X, enemy_Y]
    current_direction =[]
    count = 0 
    for move in range(2):
        enemy_coordinates = enemy_position.copy()
        for direction in direction_list:
            enemy_coordinates[move] += direction
            if not is_position_a_border(board, enemy_coordinates):
                current_direction.append(proper_directions[count])
                count += 1
    return current_direction



def enemy_move(enemy, board):
    enemy_direction = enemy_direction_move(enemy['pos_x'],enemy['pos_y'], board)
    # random.choice podpiąć do funkcji enemy_direction_move
    #  jesli random.choice bedze "w" to daj board z pozycją
    chosen_direction = random.choice(enemy_direction)
    position = ()
    if chosen_direction == "w":
        board[enemy['pos_x']][enemy['pos_y']] = ' '
        enemy['pos_x'] = enemy['pos_x'] - 1
    

    elif chosen_direction == "s":
        board[enemy['pos_x']][enemy['pos_y']] = ' '
        enemy['pos_x'] = enemy['pos_x'] + 1
  
    elif chosen_direction == "a":
        board[enemy['pos_x']][enemy['pos_y']] = ' '
        enemy['pos_y'] = enemy['pos_y'] - 1
  
    elif chosen_direction == "d":
        board[enemy['pos_x']][enemy['pos_y']] = ' '
        enemy['pos_y'] = enemy['pos_y'] + 1


def put_items_on_board(board, items):
    board[items[0]['pos_x']][items[0]['pos_y']] = items[0]['icon']
    board[items[1]['pos_x']][items[1]['pos_y']] = items[1]['icon']
    board[items[2]['pos_x']][items[2]['pos_y']] = items[2]['icon']


def item_pop(item, x):
    item.pop(x, None)


def add_to_inventory(player, item):
    item_pop(item, 'pos_y')
    item_pop(item, 'pos_x')
    item_pop(item, 'icon')
    if item["name"] not in player.keys():
        player['inventory'][item["name"]] = item
    else:
        player['inventory'][item["amount"]] += [item["amount"]]
        pass
    return player


def events(player, board, items):
    enemy_1 = creating_things.create_enemy_1()
    enemy_2 = creating_things.create_enemy_2()
    enemy_3 = creating_things.create_enemy_3()
    if board[player['pos_x']][player['pos_y']] == 'X':
        board[items[0]['pos_x']][items[0]['pos_y']] == ' '
        add_to_inventory(player, items[0])
        print('Zdobywasz klucz!')
    if board[player['pos_x']][player['pos_y']] == 'T':
        board[items[1]['pos_x']][items[1]['pos_y']] == ' '
        add_to_inventory(player, items[1])
        print('Zdobywasz miecz!')
    if board[player['pos_x']][player['pos_y']] == 'P':
        board[items[2]['pos_x']][items[2]['pos_y']] == ' '
        add_to_inventory(player, items[2])
        print('Zdobywasz miksturki!')
    if board[player['pos_x']][player['pos_y']] == '§':
        util.clear_screen()
        battle.new_battle(player, enemy_1, board)
    if board[player['pos_x']][player['pos_y']] == '¤':
        util.clear_screen()
        battle.new_battle(player, enemy_2, board)
    if board[player['pos_x']][player['pos_y']] == '°':
        util.clear_screen()
        battle.new_battle(player, enemy_3, board)

    # LVL 2
    if board[player['pos_x']][player['pos_y']] == '▒':
        pass


def create_items():
    key = creating_things.create_key()
    stick = creating_things.create_stick()
    potion1 = creating_things.create_potion(13, 13)
    return key, stick, potion1

