def display_board(board):
    for i in range(len(board)):
        for j in range(len((board)[i])):
            if j == (len((board)[i])-1):
                print(str(board[i][j]), end="\n")
            else:
                print(str(board[i][j]) + " ", end="")



def display_inventory(inventory: dict):
    print('-----------------')
    print('item name | count')
    print('-----------------')
    arr = list(inventory.items())
    arr.sort(key =lambda x: x[1])
    for line in arr:
        print('{:>9} |{:>6}'.format(*line))
    print('-----------------')

