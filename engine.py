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
    pass


def put_enemy_on_board(board):
    
    ENEMY_1_START_POS_X = 5
    ENEMY_1_START_POS_Y = 18
    ENEMY_2_START_POS_X = 15
    ENEMY_2_START_POS_Y = 20
    ENEMY_3_START_POS_X = 15
    ENEMY_3_START_POS_Y = 5
    board[ENEMY_1_START_POS_X][ENEMY_1_START_POS_Y] = '§'
    board[ENEMY_2_START_POS_X][ENEMY_2_START_POS_Y] = '§'
    board[ENEMY_3_START_POS_X][ENEMY_3_START_POS_Y] = '§'
    return board


