import cal_function
cal = cal_function.Calculator(power = 100)
cal.add(5,3)
cal.div(100 , 2)
cal.mul(5, 4)
cal.mul(3,3)

hey_dude = ['none', " ", " ", " ", " ", " ", " ", " ", " ", " "]


def check(board, position):
    if board[position] == " ":
        print("This space is available!!!")
    else:
        print("This space is already used!!!")


def player_choice():
    ans1= int(input("Hello , Please select the position..... 1 - 9:"))
    return ans1


ans = player_choice()

check(hey_dude, ans)





