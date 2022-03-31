import util
import main
def new_battle(player, enemy, board):
    util.clear_screen()
    print("Battle!\nYou are fighting againt:", enemy['name'], enemy['health'], 'HP')
    print("Your hit takes:", player['damage'])
    while True:
        enemy['health'] = enemy['health'] - player['damage']
        if enemy['health'] <= 0 and enemy['name'] == 'Boss':
                again = input('You killed the boss!\n Wanna play again? (y/n): ')
                while not again.startswith('y'):
                    main.main('board_lvl_1.txt')
        if enemy['health'] <= 0:
            print('You killed a ', enemy['name'])
            enemy['is_alive'] = False
            board[enemy['pos_x']][enemy['pos_y']] = ' '
            input('Press Enter')
            break
        else:
            print(enemy['name'], 'has ',enemy['health'], 'HP left')
            player['health'] = player['health'] - enemy['damage']
            if player['health'] <= 0:
                again = input('You died! Wanna play again? (y/n): ')
                if again.startswith('y'):
                    main.main('board_lvl_1.txt')
                else:
                    exit()
            print('You have ',player['health'], 'HP left')
            input('Press Enter')