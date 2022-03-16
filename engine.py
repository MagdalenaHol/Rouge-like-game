import util
import sys
import battle



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
    enemy_1 = create_enemy_1()
    board[enemy_1['pos_x']][enemy_1['pos_y']] = enemy_1['icon']
    enemy_2 = create_enemy_2()
    board[enemy_2['pos_x']][enemy_2['pos_y']] = enemy_2['icon']
    enemy_3 = create_enemy_3()
    board[enemy_3['pos_x']][enemy_3['pos_y']] = enemy_3['icon']

def events(player, board):
    enemy_1 = create_enemy_1()
    enemy_2 = create_enemy_2()
    enemy_3 = create_enemy_3()
    if board[player['pos_x']][player['pos_y']] == 'X':
        print('Zdobywasz klucz!')
    if board[player['pos_x']][player['pos_y']] == 'T':
        print('Zdobywasz miecz!')
    if board[player['pos_x']][player['pos_y']] == '§':
        util.clear_screen()
        battle.new_battle(player, enemy_1, board)
    if board[player['pos_x']][player['pos_y']] == '¤':
        util.clear_screen()
        battle.new_battle(player, enemy_2, board)
    if board[player['pos_x']][player['pos_y']] == ',':
        util.clear_screen()
        battle.new_battle(player, enemy_3, board)        


def create_enemy_1():    
    enemy_1 = {
        'name': "Snake",
        'health': 35,
        'damage': 20,
        'pos_x': 5,
        'pos_y': 18,
        'icon' : '§',
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