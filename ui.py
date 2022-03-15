import string
def display_board(board):
<<<<<<< HEAD
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

def get_board(file_name):
    board = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        board = [element.replace("\n", "") for element in lines]
    return board
a=get_board("board_lvl_1.txt")
#b=get_board("board_lvl_2.txt")
display_board(a)
=======
    for i in board:
        print(*i)
>>>>>>> mateusz
