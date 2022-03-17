import util
import engine
import ui
import creating_things
PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

# ENEMY_ICON = '§'
# ENEMY_START_X = 2
# ENEMY_START_Y = 2

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    player = {
        'name': "Player",
        'health': 100,
        'damage': 30,
        'pos_x': PLAYER_START_X,
        'pos_y': PLAYER_START_Y,
        'icon': PLAYER_ICON,
        'inventory': {


        }
    }
    return player


def main():
    levels = [1,2,3]
    for level in levels:    
        items = engine.create_items()
        player = create_player()
        enemy_1 = creating_things.create_enemy_1()
        board = engine.create_board('board_lvl_1.txt')
        board[5][5] = 'X'
        board[7][7] = 'T'
        util.clear_screen()
        is_running = True
        while is_running:
            engine.put_enemy_on_board(enemy_1, board) 
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
            board[old_pos_x][old_pos_y] = ' '
            util.clear_screen()
            engine.events(player, board, items)
            engine.enemy_move(enemy_1, board)


if __name__ == '__main__':
    main()
