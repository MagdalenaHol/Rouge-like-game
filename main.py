import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

# ENEMY_ICON = '§'
# ENEMY_START_X = 2
# ENEMY_START_Y = 2

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!
    Returns:
    dictionary
    '''

    player = {
        'name': "Player",
        'health': 100,
        'damage': 30,
        'pos_x': PLAYER_START_X,
        'pos_y': PLAYER_START_Y,
        'icon' : PLAYER_ICON,
        'inventory': {
                'mushroom': 1,
                'torch': 22    
        }
    }

    return player


def main():
    ENEMY_ICON = '§'
    ENEMY_START_X = 1
    ENEMY_START_Y = 2
    player = create_player()
    
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board[5][5] = 'X'
    board[7][7] = 'T'
    util.clear_screen()
    is_running = True
    while is_running:
        enemy = engine.create_enemy()
        # engine.create_enemy()
        player = create_player()
        engine.put_enemy_on_board(board) 
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        old_pos_x = player['pos_x']
        old_pos_y = player['pos_y']


        key = util.key_pressed()
        if key == 'q':
            is_running = False

        elif key == 'i':
            ui.display_inventory(player['inventory'])
            input()
        else:
            engine.movement_phase(player, key, board)
            engine.enemy_move(ENEMY_START_X, ENEMY_START_Y, board)
        # ENEMY_START_X = enemy_position[0]
        # ENEMY_START_Y = enemy_position[1]
        board[old_pos_x][old_pos_y] = ' '
        util.clear_screen()
        engine.events(player, board)


if __name__ == '__main__':
    main()