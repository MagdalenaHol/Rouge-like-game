def put_enemy_on_board(board):
    enemy_1 = creating_things.create_enemy_1()
    board[enemy_1['pos_x']][enemy_1['pos_y']] = enemy_1['icon']
    enemy_2 = creating_things.create_enemy_2()
    board[enemy_2['pos_x']][enemy_2['pos_y']] = enemy_2['icon']
    enemy_3 = creating_things.create_enemy_3()
    board[enemy_3['pos_x']][enemy_3['pos_y']] = enemy_3['icon']


