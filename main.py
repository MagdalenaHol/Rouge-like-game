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
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    actual_position = []
    while is_running:
        
        #engine.put_player_on_board(board, player)
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        actual_position = engine.movement_phase(board, player, actual_position)
        util.clear_screen()
        engine.events(player, board, items)
        engine.enemy_move(enemy_1, board)
        if 'Shovel' in player['inventory'] and board[player['pos_x']][player['pos_y']] == '×':
            return True


if __name__ == '__main__':
    main()