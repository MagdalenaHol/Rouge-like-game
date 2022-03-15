import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = '@'
    return player


def main():
    player = create_player()
    start_position = [3, 3]
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    actual_position = []
    while is_running:
        #print(actual_position)
        if len(actual_position) > 2:
            del actual_position[0]
            del actual_position[0]
        #engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        if key == 'd':
            if len(actual_position) == 0:
                board[start_position[0]][start_position[1] + 1] = player
                actual_position.append(start_position[0])
                actual_position.append(start_position[1] + 1)
            elif len(actual_position) > 0:
                board[actual_position[0]][actual_position[1] + 1] = player
                actual_position.append(actual_position[0])
                actual_position.append(actual_position[1] + 1)
                board[actual_position[0]][actual_position[1]] = '.'
        if key == 's':
            if len(actual_position) == 0:
                board[start_position[0] + 1][start_position[1]] = player
                actual_position.append(start_position[0] + 1)
                actual_position.append(start_position[1])
            elif len(actual_position) > 0:
                board[actual_position[0] + 1][actual_position[1]] = player
                actual_position.append(actual_position[0] + 1)
                actual_position.append(actual_position[1])
                board[actual_position[0]][actual_position[1]] = '.'
        if key == 'a':
            if len(actual_position) == 0:
                board[start_position[0]][start_position[1] - 1] = player
                actual_position.append(start_position[0])
                actual_position.append(start_position[1] - 1)
            elif len(actual_position) > 0:
                board[actual_position[0]][actual_position[1] - 1] = player
                actual_position.append(actual_position[0])
                actual_position.append(actual_position[1] - 1)
                board[actual_position[0]][actual_position[1]] = '.'
        if key == 'w':
            if len(actual_position) == 0:
                board[start_position[0] - 1][start_position[1]] = player
                actual_position.append(start_position[0] - 1)
                actual_position.append(start_position[1])
            elif len(actual_position) > 0:
                board[actual_position[0] - 1][actual_position[1]] = player
                actual_position.append(actual_position[0] - 1)
                actual_position.append(actual_position[1])
                board[actual_position[0]][actual_position[1]] = '.'
        util.clear_screen()


if __name__ == '__main__':
    main()
