import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

ENEMY_ICON = "E"
ENEMY_START_X = 4
ENEMY_START_Y = 4

BOARD_WIDTH = 30
BOARD_HEIGHT = 20



<<<<<<< HEAD
def create_player():
    player = "@"
=======
    Returns:
    dictionary
    '''
    player = '@'
>>>>>>> origin/Mateusz
    return player


def main():
    player = create_player(PLAYER_START_X, PLAYER_START_Y)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    actual_position = []
    while is_running:
<<<<<<< HEAD
        enemy = engine.create_enemy(ENEMY_ICON,ENEMY_START_X,ENEMY_START_Y)
        engine.put_player_on_board(board, player)
        engine.put_enemy_on_board(board,enemy)
=======
        
        #engine.put_player_on_board(board, player)
>>>>>>> origin/Mateusz
        ui.display_board(board)
        key = util.key_pressed()
        if key == 'q':
            is_running = False
        actual_position = engine.movement_phase(board, player, actual_position)
        util.clear_screen()


if __name__ == '__main__':
    main()
