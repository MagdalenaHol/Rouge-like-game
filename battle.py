import engine
import util
import main
def new_battle(player, enemy, board):
    util.clear_screen()
    print("Battle!")
    attack = input('Do you want to attack? (y/n): ').lower()
    if attack.startswith('y'):
        while True:
            enemy['health'] = enemy['health'] - player['damage']
            if enemy['health'] < 0:
                print('You killed a ', enemy['name'])
                print(enemy)
                enemy.clear() 
            else:
                player['health'] = player['health'] - enemy['damage']
                if player['health'] < 0:
                    again = ('You died! Wnna play again? (y/n): ')
                    if again.startswith('y'):
                        main.main()
    
    if attack.startswith('n'):
        enemy = engine.put_enemy_on_board(board)