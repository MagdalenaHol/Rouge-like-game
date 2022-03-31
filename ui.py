import colorama
from colorama import Fore,Back, Style
colorama.init()
def display_board(board):
    for i in range(len(board)):
        for j in range(len((board)[i])):
            if j == (len((board)[i])-1):
                print(Fore.GREEN + str(board[i][j]), end="\n")
            else:
                print(Fore.GREEN + str(board[i][j]) + " ", end="")


def display_inventory(inventory):
    for key, value in inventory.items():
        print(Fore.CYAN + '{}: {}'.format(key, value, end="\n"))    
