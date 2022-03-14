def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    pass


def display_inventory(inventory: dict):
    print('-----------------')
    print('item name | count')
    print('-----------------')
    arr = list(inventory.items())
    arr.sort(key =lambda x: x[1])
    for line in arr:
        print('{:>9} |{:>6}'.format(*line))
    print('-----------------')
