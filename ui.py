import string

def display_board(board):
    for i in range(len(board)):
        for j in range(len((board)[i])):
            if j == (len((board)[i])-1):
                print(str(board[i][j]), end="\n")
            else:
                print(str(board[i][j]) + " ", end="")



def display_inventory(inventory):
    for key, value in inventory.items():
        print('{}: {}'.format(key, value, end="\n"))    
<<<<<<< HEAD


=======
>>>>>>> 085ccc4499acfdf6fe2e2f9636b7ccb001b4d7a0

