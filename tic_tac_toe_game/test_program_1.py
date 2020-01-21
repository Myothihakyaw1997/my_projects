import time
def display_board(board):
    print( f"{board[1]}  |  {board[2]}  | {board[3]}")
    print( f"{board[4]}  |  {board[5]}  | {board[6]}")
    print( f"{board[7]}  |  {board[8]}  | {board[9]}")
test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)
print(" ")
print(" ")

def player_input():
    conn = True
    while conn:
        pos = input("Please select position  'X' or 'O': ")
        if pos == 'X' or pos == 'O':
            conn = False
            return pos
        else:
            print("The invalid position or keyword !!!")
            conn = True
        time.sleep(1.5)

player_input()


def place_marker(board, marker, position):
    board[position] = marker

place_marker(test_board,'X',8)
display_board(test_board)


def win_check(board, mark):
    board[1:4] = [mark ,mark , mark]
    if board[1:4] == [mark,mark,mark] or board[4:7] == [mark,mark,mark] or board[7:10] == [mark,mark,mark]:
        print("The player x is the winner!")
        return True
    else:
        return False

win_check(test_board,'X')
import random
def choose_first():
     ans =  random.randint(1,2)
     return ans
result = choose_first()
result


def space_check(board, position):
    if board[position] == " ":
        pass
    else:
        print("The space is already used!!")
space_check(test_board,8)


def full_board_check(board):
    for i in test_board:
        if i  == " ":
            pass
        else:
            return False
            break
        return True

full_board_check(test_board)


def player_choice(board):
    con = True
    while con:

        player_position = int(input("Choose the next position ----(1 - 9) : "))
        if board[player_position] == " ":
            con = False
        else:
            print("The space is already used!!")
            con = True
        return player_position
player_choice(test_board)


def replay():
   con = True
   while con:
        player_decision = input("Do you want to replay this game ? yes or no ?")
        if player_decision =="yes":
            return True
            con = False
        elif player_decision =="no":
            return False
            con = False
        else:

            print("Invalid answer.Please write 'yes' or 'no'")
            con = True



replay()
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker = player_input()
    player2_marker = player_input()
    turn = choose_first()
    turn1 = str(turn)
    print(turn1 + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break




