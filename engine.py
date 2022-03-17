import util
import sys
import random

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

def put_enemy_on_board(board):
    enemy = create_enemy()
    board[enemy['pos_x']][enemy['pos_y']] = enemy['icon']




def is_position_a_border(board, coordinates):
    coordinates_on_board = board[coordinates[0]][coordinates[1]]
    return coordinates_on_board == ['|'] or coordinates_on_board == ['-'] or coordinates_on_board == [" "] 


def enemy_direction_move(board, enemy_start_x, enemy_start_y):
    proper_directions = ["up", "down", "left", "right"]
    # direction_list = ((-1, 0), (1, 0), (0, 1), (0, -1))
    direction_list = [-1,2]
    enemy_position = [enemy_start_x, enemy_start_y]
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



def enemy_move(board, enemy_start_x, enemy_start_y):
    enemy_direction = enemy_direction_move(board, enemy_start_x, enemy_start_y)
    # random.choice podpiąć do funkcji enemy_direction_move
    #  jesli random.choice bedze "up" to daj board z pozycją
    chosen_direction = random.choice(enemy_direction)
    position = ()
    if chosen_direction == "up":
        board[enemy_start_x][enemy_start_y] = ' '
        enemy_start_x = enemy_start_x - 1
        position = (enemy_start_x, enemy_start_y)
        return position

    elif chosen_direction == "down":
        board[enemy_start_x][enemy_start_y] = ' '
        enemy_start_x = enemy_start_x + 1
        position = (enemy_start_x, enemy_start_y)
        return position

    elif chosen_direction == "left":
        board[enemy_start_x][enemy_start_y] = ' '
        enemy_start_y = enemy_start_y - 1
        position = (enemy_start_x, enemy_start_y)
        return position

    elif chosen_direction == "right":
        board[enemy_start_x][enemy_start_y] = ' '
        enemy_start_y = enemy_start_y + 1
        position = (enemy_start_x, enemy_start_y)
        return position




def events(player, board):
    if board[player['pos_x']][player['pos_y']] == 'X':
        print('Zdobywasz klucz!')
    if board[player['pos_x']][player['pos_y']] == 'T':
        print('Zdobywasz miecz!')
    if board[player['pos_x']][player['pos_y']] == '§':
        util.clear_screen()
        #battle.new_battle(player, enemy())


