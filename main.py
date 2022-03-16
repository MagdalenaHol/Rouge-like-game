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

    player = {
        'name': "Player",
        'health': 100,
        'damage': 30,
        'pos_x': PLAYER_START_X,
        'pos_y': PLAYER_START_Y,
        'icon' : PLAYER_ICON,
        'inventory': {
                
                   
        }
    }

    return player

#def add_to_inventory(player):
#    pass


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    items = engine.create_items()
    engine.put_items_on_board(board,items)
    #board[5][5] = 'X'
    #board[7][7] = 'T'
    util.clear_screen()
    is_running = True
    #actual_position = []
    while is_running:
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
            input("press enter to exit inventory")
        else:
            engine.movement_phase(player, key, board)
        board[old_pos_x][old_pos_y] = ' '
        util.clear_screen()
        engine.events(player, board,items)

if __name__ == '__main__':
    main()