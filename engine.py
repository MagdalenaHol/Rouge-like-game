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

    board = []

    for i in range(height):
        board.append(['.'] * width)
    return board

    









def put_player_on_board(board, player):
    board[3][3] = player
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    return player




def movement_phase(board, player):
    start_position = [3, 3]
    actual_position = []
    print(actual_position)
    key = util.key_pressed()
    if len(actual_position) > 1:
            del actual_position[0]
    if key == 'd':
        if len(actual_position) == 0:
                board[start_position[0]][start_position[1] + 1] = player
                actual_position.append((start_position[0], start_position[1] + 1))
        elif len(actual_position) > 0:
                board[actual_position[0][0]][actual_position[0][1] + 1] = player
                actual_position.append((actual_position[0][0], actual_position[0][1] + 1))
                board[actual_position[0][0]][actual_position[0][1]] = '.'
                print(actual_position)
    if key == 's':
        if len(actual_position) == 0:
            board[start_position[0] + 1][start_position[1]] = player
            actual_position.append((start_position[0] + 1, start_position[1]))
        elif len(actual_position) > 0:
            board[actual_position[0][0] + 1][actual_position[0][1]] = player
            actual_position.append((actual_position[0][0] + 1, actual_position[0][1]))
            board[actual_position[0][0]][actual_position[0][1]] = '.'
    if key == 'a':
        if len(actual_position) == 0:
            board[start_position[0]][start_position[1] - 1] = player
            actual_position.append((start_position[0], start_position[1] - 1))
        elif len(actual_position) > 0:
            board[actual_position[0][0]][actual_position[0][1] - 1] = player
            actual_position.append((actual_position[0][0], actual_position[0][1] - 1))
            board[actual_position[0][0]][actual_position[0][1]] = '.'
    if key == 'w':
        if len(actual_position) == 0:
            board[start_position[0] - 1][start_position[1]] = player
            actual_position.append((start_position[0] - 1, start_position[1]))
        elif len(actual_position) > 0:
            board[actual_position[0][0] - 1][actual_position[0][1]] = player
            actual_position.append((actual_position[0][0] - 1, actual_position[0][1]))
            board[actual_position[0][0]][actual_position[0][1]] = '.'
    return actual_position