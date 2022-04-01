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


def put_enemy_on_board(enemy, board):
    if enemy['is_alive']:
        board[enemy['pos_x']][enemy['pos_y']] = enemy['icon']
    if not enemy['is_alive']:
        board[enemy['pos_x']][enemy['pos_y']] = ' '

def put_boss_on_board(boss, board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 'B':
                board[row][column] = ' '
    for i in range(5):
        board[boss["pos_x"] + i][boss["pos_y"]] = boss["icon"]
        for j in range(5):
            board[boss["pos_x"] + i][boss["pos_y"] + j] = boss["icon"]


def player_move(player, key, board):
    obstacles = ['|', '_', '*', '^']
    while True:
        if key == 'w':
            if player["name"] == 'Boss':
                for i in range(5):
                    if board[player["pos_x"] - 1][player["pos_y"] + i] in obstacles:
                        break
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


def enemy_move(enemy, board):
    obstacles = ['|', '_', '*', '^', 'x', 'T', 'X']
    chosen_direction = random.choice(['w', 's', 'a', 'd'])
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


def events(player, board, items, enemy_1, enemy_2, enemy_3, boss):

    item = board[player['pos_x']][player['pos_y']]
    if item == 'X':
        board[items[0]['pos_x']][items[0]['pos_y']] == ' '  
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
    if item == 'B':
        util.clear_screen()
        battle.new_battle(player, boss, board)
