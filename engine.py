import util
import sys
import random
import create
import battle
import copy
import ui


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


def put_enemy_on_board(enemy_1, board):
    board[enemy_1['pos_x']][enemy_1['pos_y']] = enemy_1['icon']


def movement_phase(player, key, board):
    obstacles = ['|', '_', '*', '^']
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


def is_position_a_border(board, coordinates):
    coordinates_on_board = board[coordinates[0]][coordinates[0]]
    return coordinates_on_board == ['|'] or coordinates_on_board == ['_'] or coordinates_on_board == ['^'] or coordinates_on_board == ['*']


def enemy_direction_move(enemy_X, enemy_Y, board):
    proper_directions = ["w", "s", "a", "d"]
    direction_list = [1, 2]
    enemy_position = [enemy_X, enemy_Y]
    current_direction = []
    count = 0
    for move in range(2):
        enemy_coordinates = copy.deepcopy(enemy_position)
        for direction in direction_list:
            enemy_coordinates[move] += direction
            if not is_position_a_border(board, enemy_coordinates):
                current_direction.append(proper_directions[count])
                count += 1
    return current_direction


def enemy_move(enemy, board):
    obstacles = ['|', '_', '*', '^']
    enemy_direction = enemy_direction_move(
        enemy['pos_x'], enemy['pos_y'], board)
    chosen_direction = random.choice(enemy_direction)
    while True:
        if chosen_direction == "w":
            if board[enemy['pos_x']-1][enemy['pos_y']] in obstacles:
                break
            else:
                board[enemy['pos_x']][enemy['pos_y']] = ' '
                enemy['pos_x'] = enemy['pos_x'] - 1
                break
        elif chosen_direction == "s":
            if board[enemy['pos_x']+1][enemy['pos_y']] in obstacles:
                break
            else:
                board[enemy['pos_x']][enemy['pos_y']] = ' '
                enemy['pos_x'] = enemy['pos_x'] + 1
                break
        elif chosen_direction == "a":
            if board[enemy['pos_x']][enemy['pos_y']-1] in obstacles:
                break
            else:
                board[enemy['pos_x']][enemy['pos_y']] = ' '
                enemy['pos_y'] = enemy['pos_y'] - 1
                break
        elif chosen_direction == "d":
            if board[enemy['pos_x']][enemy['pos_y']+1] in obstacles:
                break
            else:
                board[enemy['pos_x']][enemy['pos_y']] = ' '
                enemy['pos_y'] = enemy['pos_y'] + 1
                break


def get_old_position(player, enemy_1):
    old_pos_x = player['pos_x']
    old_pos_y = player['pos_y']
    enemy_1_old_pos_x = enemy_1['pos_x']
    enemy_1_old_pos_y = enemy_1['pos_y']
    return old_pos_x, old_pos_y, enemy_1_old_pos_x, enemy_1_old_pos_y


def put_items_on_board(board, items):
    board[items[0]['pos_x']][items[0]['pos_y']] = items[0]['icon']
    board[items[1]['pos_x']][items[1]['pos_y']] = items[1]['icon']
    board[items[2]['pos_x']][items[2]['pos_y']] = items[2]['icon']
    board[items[3]['pos_x']][items[3]['pos_y']] = items[3]['icon']


def create_items():
    shovel = create.create_shovel()
    stick = create.create_stick()
    potion1 = create.create_potion(2, 2)
    mushroom = create.create_mushroom(4, 3)
    return shovel, stick, potion1, mushroom


def add_to_inventory(player, item):
    item_ = copy.deepcopy(item)
    """item_pop(item_, 'pos_y')
    item_pop(item_, 'pos_x')
    item_pop(item_, 'icon')"""
    if item_["name"] not in player.keys():
        player['inventory'][item_["name"]] = item_
    else:
        player['inventory'][item_["amount"]] += [item_["amount"]]


def using_items(player: dict):
    print()
    if len(player['inventory']) != 0:
        print("items you can use:")
        for name, items in player['inventory'].items():
            for k, v in items.items():
                if k == "usable" and v == "yes":

                    print()
                    ui.display_items(items)
        print("Enter first letter of item you wanna use")
        char = util.key_pressed()
        for name, items in player['inventory'].items():
            if items["name"][0] == char.upper():
                player["health"] += items["healing"]
                items["amount"] -= 1


def check_amount(player: dict):
    for key, items in player.items():
        if items["amount"] == 0:
            player.pop(items["name"].capitalize())
            break


def events(player, board, items):
    enemy_1 = create.create_enemy_1()
    enemy_2 = create.create_enemy_2()
    enemy_3 = create.create_enemy_3()
    item = board[player['pos_x']][player['pos_y']]
    if item == 'X':
        board[items[0]['pos_x']][items[0]['pos_y']
                                 ] == ' '  # TODO remove from board
        add_to_inventory(player, items[0])
        print('Zdobywasz łopatę!')
    if item == 'T':
        board[items[1]['pos_x']][items[1]['pos_y']] == ' '
        add_to_inventory(player, items[1])
        player["damage"] += items[1]["damage"]
        print('Zdobywasz patyk!')
    if item == 'P':
        board[items[2]['pos_x']][items[2]['pos_y']] == ' '
        add_to_inventory(player, items[2])
        print('Zdobywasz 3 jagody!')
    if item == 'M':
        board[items[3]['pos_x']][items[3]['pos_y']] == ' '
        add_to_inventory(player, items[3])
        print('Zdobywasz 3 grzyby!')
    if item == '§':
        util.clear_screen()
        battle.new_battle(player, enemy_1, board)
    if item == '¤':
        util.clear_screen()
        battle.new_battle(player, enemy_2, board)
    if item == ',':
        util.clear_screen()
        battle.new_battle(player, enemy_3, board)

    # LVL 2
    if item == '×':
        pass
