import util
import engine
import ui
import create
PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
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


def main(level):    
    items = engine.create_items()
    player = create_player()
    enemy_1 = create.create_enemy_1()
    enemy_2 = create.create_enemy_2()
    enemy_3 = create.create_enemy_3()
    board = engine.create_board(level)
    board[19][29] = '×'
    board[5][5] = 'X'
    board[7][7] = 'T'
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        """ LVL_1 """
        engine.put_enemy_on_board(enemy_1, board) 
        """ LVL_2 """
        if level == 'board_lvl_2.txt':
            engine.put_enemy_on_board(enemy_2, board)
            engine.put_enemy_on_board(enemy_3, board)
        """ LVL_3 """    
        if level == 'board_lvl_3.txt':           
            engine.put_boss_on_board()                             
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
        if 'shovel' in player['inventory'] and board[player['pos_x']][player['pos_y']] == '×':
            return True


if __name__ == '__main__':
    levels = ['board_lvl_1.txt', 'board_lvl_2.txt', 'board_lvl_3.txt']
    for level in levels:
        main(level)



