
def put_enemy_on_board(board):
    enemy_1 = creating_things.create_enemy_1()
    board[enemy_1['pos_x']][enemy_1['pos_y']] = enemy_1['icon']
    enemy_2 = creating_things.create_enemy_2()
    board[enemy_2['pos_x']][enemy_2['pos_y']] = enemy_2['icon']
    enemy_3 = creating_things.create_enemy_3()
    board[enemy_3['pos_x']][enemy_3['pos_y']] = enemy_3['icon']




def movement_phase(board, player, actual_position):
    start_position = [3, 3]
    actual_position = []
    print(actual_position)
    key = util.key_pressed()
    if len(actual_position) > 1:
            del actual_position[0]
    if key == 'd':
        if len(actual_position) == 0:
                board[start_position[0]][start_position[1] + 1] = player
                actual_position.append((start_position[0], start_position[1] + 1))
        elif len(actual_position) > 0:
                board[actual_position[0][0]][actual_position[0][1] + 1] = player
                actual_position.append((actual_position[0][0], actual_position[0][1] + 1))
                board[actual_position[0][0]][actual_position[0][1]] = '.'
                print(actual_position)
                #print(actual_position)
    if key == 's':
        if len(actual_position) == 0:
            board[start_position[0] + 1][start_position[1]] = player
            actual_position.append((start_position[0] + 1, start_position[1]))
        elif len(actual_position) > 0:
            board[actual_position[0][0] + 1][actual_position[0][1]] = player
            actual_position.append((actual_position[0][0] + 1, actual_position[0][1]))
            board[actual_position[0][0]][actual_position[0][1]] = '.'
    if key == 'a':
        if len(actual_position) == 0:
            board[start_position[0]][start_position[1] - 1] = player
            actual_position.append((start_position[0], start_position[1] - 1))
        elif len(actual_position) > 0:
            board[actual_position[0][0]][actual_position[0][1] - 1] = player
            actual_position.append((actual_position[0][0], actual_position[0][1] - 1))
            board[actual_position[0][0]][actual_position[0][1]] = '.'
    if key == 'w':
        if len(actual_position) == 0:
            board[start_position[0] - 1][start_position[1]] = player
            actual_position.append((start_position[0] - 1, start_position[1]))
        elif len(actual_position) > 0:
            board[actual_position[0][0] - 1][actual_position[0][1]] = player
            actual_position.append((actual_position[0][0] - 1, actual_position[0][1]))


            