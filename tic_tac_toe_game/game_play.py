import random
import time
def display_board(board):
                    print( f"{board[1]}  |  {board[2]}  | {board[3]}")
                    print( f"{board[4]}  |  {board[5]}  | {board[6]}")
                    print( f"{board[7]}  |  {board[8]}  | {board[9]}")

examble_board = [0,1,2,3,4,5,6,7,8,9]
def player_input():
    conn = True
    while conn:
        marker = input(f" Its {players}. Please select marker 'X' or 'O': ")
        if marker == 'X' or marker == 'O':
            conn = False
            return marker
        else:
            print("The invalid marker or keyword !!!")
            conn = True

def choose_first():
    check = True
    while check:
        ch_f = input(f"who gonna go first ? {player1_name}(player1) or {player2_name}(player2) ; just write 1 or 2 ")
        if ch_f in ['1', '2']:
            check = False
            return ch_f
        else:
            print("Invalid word")
            check = True

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
def space_check(board, position):
    if board[position]== " ":
        return True
    else:
        return False


def full_board_check(board):
    if (board[1] == " " or board[2] == " " or board[3] == " " or
            board[4] == " " or board[5] == " " or board[6] == " " or
            board[7] == " " or board[8] == " " or board[9] == " "):
        return True
    else:
        return False
def player_choice():
    val = True
    l1 = ['1','2','3','4','5','6','7','8','9']
    while val:
        player_pos = input("Choose your position..... 1 - 9:")
        if player_pos  in l1:
              val = False
              return int(player_pos)
        else:
            val = True
            print("Invalid number or keywords!!!")
def replay():
    var2 = True
    while var2:
        ans1 = input("Do you want to replay the game , just say 'yes' or 'no' : ")
        if ans1 == "yes":
            var2 = False
            return True
        elif ans1 == "no":
            var2 = False
            return False
        else:
            print("Invalid word")
            var2 = True
def play_tutorial():
    dec1 = input("Do you want to watch tutorial before playing game ? just write 'yes  or no'.")
    if dec1 =="yes":
        print("Tic Tac Toe Version 1.00 ")
        time.sleep(2)
        print("In this game , players must choose the numbers between 1 - 9 for place marking on the board ")
        time.sleep(2)
        print("The below figure show how the numbers are configure on the board ")
        time.sleep(3)
        display_board(examble_board)
        time.sleep(2)
        print("Two player is needed to play the game ")
        time.sleep(3)
        print("The player must wait after choosing the desire number for the other player turn ")
        time.sleep(3)
        print("The game will be shut down automatically , when the board is full or the player  won")
        time.sleep(2)
        print("If u want to know more about the gameplay , just search 'How to play the tic tac toe game' in google" )
        time.sleep(1)
    elif dec1 == "no":
        print("Ok , I assume u know the basic..")
    else:
        print("Dont know what's you are writing about. but i assume u don't want to watch tutorial about the game")

def availabe_position(board1):
    avai_list = []
    if board1[1] == " ":
        avai_list.append(1)
    if board1[2] == " ":
        avai_list.append(2)
    if board1[3] == " ":
        avai_list.append(3)
    if board1[4] == " ":
        avai_list.append(4)
    if board1[5] == " ":
        avai_list.append(5)
    if board1[6] == " ":
        avai_list.append(6)
    if board1[7] == " ":
        avai_list.append(7)
    if board1[8] == " ":
        avai_list.append(8)
    if board1[9] == " ":
        avai_list.append(9)
    print(f"avilable spaces are {str(avai_list)} ")

print('Welcome to Tic Tac Toe!!')
play_tutorial()
player1_name = input("Choose name for player 1 :")
player2_name = input("Choose name for player 2 :")
Start = True
while Start:
    game_status = True
    real_board = ['none', " ", " ", " ", " ", " ", " ", " ", " ", " "]
    start = True
    player1_turn = False
    player2_turn = False
    while start:
        game_on = False
        player1 = False
        player2 = False
        player_ans = input("Are you ready to play game ? yes or no :")
        if player_ans == "yes":
            start = False
            game_on = True
        elif player_ans == "no":
            print("Ok as u like , just say 'yes' when u want to start !!")
            start = True
    time.sleep(1)
    print("loading please wait")
    for t in range(4):
        print(t)
        time.sleep(1)
    print("Now lets see who is the one to choose marker first by random  !!")
    time.sleep(1)
    print("Shuffling in ")
    for q in range(1,4):
        print(q)
        time.sleep(1)
    rad1 =random.randint(1,2)
    time.sleep(1)
    if rad1 == 1:
        players = player1_name
        symbol = player_input()
        if symbol == "X":
            player1 = symbol
            player2 = "O"
            print(f"{player1_name} is {player1}")
            time.sleep(1)
            print(f"{player2_name} is O ")
        elif symbol == "O":
            player1 = symbol
            player2 = "X"
            print(f"{player2_name} is X")
            time.sleep(1)
            print(f"{player1_name} is O ")
    if rad1 == 2:
        players = player2_name
        symbol = player_input()
        if symbol == "X":
            player2 = symbol
            player1 = "O"
            print(f"{player2_name} is {player2}")
            time.sleep(1)
            print(f"{player1_name} is O ")
        elif symbol == "O":
            player2 = symbol
            player1 = "X"
            print(f"{player1_name} is X")
            time.sleep(1)
            print(f"{player2_name} is O ")
    time.sleep(1)
    while game_on:
        if game_status==True:
            time.sleep(1)
            print("Loading please wait")
            for l in range(1, 4):
                print(l)
                time.sleep(1)
            rad = choose_first()
            if rad == "1":
                player1_turn = True
                print(f"{player1_name} gonna go first !!")
            elif rad == "2":
                player2_turn = True
                print(f"{player2_name} gonna go first !!")
            else:
                pass
            time.sleep(1)
        while player1_turn:
            time.sleep(1)
          #  print(f"{player1_name} turn")
            display_board(real_board)
            '''For asking the correct answer again and agani until we got the right one!!
               I use while method for asking right answer , if the answer correct, while loop will break'''
            pos_choice1 = True
            while pos_choice1:
                q1 = player_choice()
                spaceCheck = space_check(real_board, q1)
                if spaceCheck == True:
                    place_marker(real_board, player1, q1)
                    real_board[q1] = player1
                    pos_choice1 = False
                else:
                     print("The space is already used !!!")
                     time.sleep(1)
                     availabe_position(real_board)
                     time.sleep(1)
                     display_board(real_board)
                     pos_choice1 = True
            '''full_board_check function is used to check whether the board or not '''
            f_board = full_board_check(real_board)
            if f_board ==False:
                print("there is no space left")
                print("No one win.Its draw")
                player1_trun = False
                player2_turn = False
                game_on = False
                break
            '''Win check is used for whether you have won the match or not'''
            if win_check(real_board, player1):
                display_board(real_board)
                print(f"congratulation {player1_name}. You have won the match ")
                player1_turn = False
                player2_turn = False
                game_on = False
                break
            #display_board(real_board)
            player1_turn= False
            player2_turn = True
            game_status = False
            time.sleep(1)
            print(f"Now {player2_name} turn ")
            time.sleep(1)
        while player2_turn:
            time.sleep(1)
           # print(f"{player2_name} turn")
            display_board(real_board)
            pos_choice2 = True
            while pos_choice2:
                q2 = player_choice()
                spaceCheck = space_check(real_board, q2)
                if spaceCheck == True:
                    place_marker(real_board, player1, q2)
                    real_board[q2] = player2
                    pos_choice2 = False
                else:
                     print("The space is already used !!!")
                     time.sleep(1)
                     availabe_position(real_board)
                     time.sleep(1)
                     display_board(real_board)
                     pos_choice2 = True
            f_board = full_board_check(real_board)
            if  f_board == False:
                print("There is no space left")
                print("No one win.Its draw")
                player2_turn = False
                player1_turn = False
                game_on = False
                break
            if win_check(real_board, player2):
                display_board(real_board)
                print(f"congratulation {player2_name}. You have won the match")
                player1_turn = False
                player2_turn = False
                game_on = False
                break
            #display_board(real_board)
            player2_turn = False
            player1_turn = True
            game_status = False
            time.sleep(1)
            print(f"Now {player1_name} turn")
            time.sleep(1)
    time.sleep(1)
    player_decision = replay()
    if player_decision == True:
        Start = True

    else:
        print("Thanks for playing the game :)")
        Start = False
        time.sleep(1)
        print("The game is closing in")
        time.sleep(1)
        for t1 in range(4):
            print(t1)
            time.sleep(1)

