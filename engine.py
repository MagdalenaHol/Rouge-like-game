import util
    

def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''



def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    # pass

def create_enemy(enemy_sybol, enemy_start_x, enemy_start_y):
    enemy_sybol = "E"
    enemy = {}
    enemy[enemy_sybol] = [enemy_start_x, enemy_start_y]
    return enemy


def put_enemy_on_board(board, enemy):
    enemy_coordinates = list(enemy.values())
    enemy_symbol = list(enemy.keys())
    enemy_coordinate_x = enemy_coordinates[0][0]
    enemy_coordinate_y = enemy_coordinates[0][1]
    board[enemy_coordinate_x][enemy_coordinate_y] = enemy_symbol
    
    return board

