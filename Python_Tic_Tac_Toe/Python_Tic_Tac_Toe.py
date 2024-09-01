
print("Tic Tac Toe")

board = {1 : " ", 2 : " ", 3 : " ", 
         4 : " ", 5 : " ", 6 : " ",
         7 : " ", 8 : " ", 9 : " "}

def print_board(board):

    print(board[1] + "_|_" + board[2] + "_|_" + board[3])
    print(board[4] + "_|_" + board[5] + "_|_" + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])



def player_input(player):

     number = input()
     
     board[int(number)] = player


def player_turn(player):

    if player == 'X':
        player = player.replace('X', 'O')
    else:
        player = player.replace('O', 'X')



def check_win(board):

    return False

def game():

    turns = 0

    player = 'X'

    while(turns < 9):
       print_board(board)
       player_input(player)
       player_turn(player)
       check_win(board)
       turns += 1

    print_board(board)

game()

