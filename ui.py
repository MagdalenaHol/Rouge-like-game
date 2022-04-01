# from rich import print

def display_board(board):
    for i in range(len(board)):
        for j in range(len((board)[i])):
            if j == (len((board)[i])-1):
                print(str(board[i][j]), end="\n")
            else:
                print(str(board[i][j]) + " ", end="")


def display_inventory(inventory):

    for key, value in inventory.items():
        print('{}: '.format(key,  end="\n"))
        for k, v in value.items():
            if k in dont_display():
                pass
            else:
                print(' {} : {} '.format(k, v,  end="\n"))


def dont_display():
    tab = ["name", "usable", 'pos_y', 'pos_x', 'icon']
    return tab


def display_items(items):
    for key, value in items.items():
        if key != "usable":
            if key == "name":
                print( ' {}'.format(value,  end="\n"))
            elif key not in dont_display():
                print(' {} : {} '.format(key, value,  end="\n"))
