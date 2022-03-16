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
    enemy = create_enemy()
    board[enemy['pos_x']][enemy['pos_y']] = enemy['icon']


def events(player, board):
    enemy = create_enemy()

    if board[player['pos_x']][player['pos_y']] == 'X':
        print('Zdobywasz klucz!')
    if board[player['pos_x']][player['pos_y']] == 'T':
        print('Zdobywasz miecz!')
    if board[player['pos_x']][player['pos_y']] == '§':
        print('Zdobywasz miecz!')
        util.clear_screen()
        battle.new_battle(player, enemy, board)


def create_enemy():    
    enemy_1 = {
        'name': "Snake",
        'health': 35,
        'damage': 30,
        'pos_x': 5,
        'pos_y': 18,
        'icon' : '§',
        }
    return enemy_1