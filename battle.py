import engine
import util
import main
def new_battle(player, enemy):
    player = main.create_player()
    enemy = engine.create_enemy()
    util.clear_screen()
    print("Battle!")
    attack = input('Do you want to attack? (y/n): ').lower()
    while not attack.startswith('y') or attack.startswith('n'):
        attack = input('Do you want to attack? (y/n): ').lower()
    if attack.startswith('y'):
        enemy['health'] = enemy['health'] - player['damage']
        if enemy['health'] < 0:
            print('You killed a ', enemy['name'])
            print(enemy)
            enemy.clear()  
    if attack.startswith('n'):
        print('exit')
        exit()

            
            
