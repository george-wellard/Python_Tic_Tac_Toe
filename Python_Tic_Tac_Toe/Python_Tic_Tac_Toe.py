
print("Tic Tac Toe")

board = {1 : " ", 2 : " ", 3 : " ", 
         4 : " ", 5 : " ", 6 : " ",
         7 : " ", 8 : " ", 9 : " "}

def print_board(board):

    print(board[1] + "_|_" + board[2] + "_|_" + board[3])
    print(board[4] + "_|_" + board[5] + "_|_" + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])

def wipe_board(board):
    
    for space in board:
        board[space] = ' '

def player_input(player):

    print("It's " + player + " 's turn")

    turn_over = False;

    while(turn_over is False):
        number = input()
        
        if(board[int(number)] == ' '):
            board[int(number)] = player
            turn_over = True
        else:
           print("This position has been taken")
           print("Enter a different number")

def game():

    turns = 0
    current_player = 'X'
    win = False
    playing = True

    while (playing):

        while(turns < 9):

            print_board(board)
            player_input(current_player)
            # Checking each board combination to see if they've been filled with a straight row of X's or O's and then announcing a winner and ending the loop

            if board[1] == board[2] and board[1] == board[3] and board[1] == 'X' or board[1] == board[2] and board[1] == board[3] and board[1] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[4] == board[5] and board[4] == board[6] and board[4] == 'X' or board[4] == board[5] and board[4] == board[6] and board[4] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[7] == board[8] and board[7] == board[9] and board[7] == 'X' or board[7] == board[8] and board[7] == board[8] and board[7] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[1] == board[4] and board[1] == board[7] and board[1] == 'X' or board[1] == board[4] and board[1] == board[7] and board[1] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[2] == board[5] and board[2] == board[8] and board[2] == 'X' or board[2] == board[5] and board[2] == board[8] and board[2] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[3] == board[6] and board[3] == board[9] and board[3] == 'X' or board[3] == board[6] and board[3] == board[9] and board[3] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[1] == board[5] and board[1] == board[9] and board[1] == 'X' or board[1] == board[5] and board[1] == board[9] and board[1] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break
            elif board[3] == board[5] and board[3] == board[7] and board[3] == 'X' or board[3] == board[5] and board[3] == board[7] and board[3] == 'O':
                print("Game Over")
                print(current_player + " has won!")
                win = True
                break

            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            turns += 1

        print_board(board)

        if win is False:
            print("Draw!")

        print("Would you like to play again?")
        print("Type y for yes or n for no")
        new_game = input()

        if new_game == 'y':
            print("New Game!")
            wipe_board(board)
            turns = 0
        else:
            playing = False

game()
print("Thanks for playing!")