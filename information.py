import time as t
userid = input("What is your name :")
total_cards = 52
def draw_card():
     global total_cards
     total_cards = total_cards - c
     print(f"You have draw {c} from the desk")
     t.sleep(1)
     print(f"the remaining cards : {total_cards}")
     t.sleep(1)
     return total_cards
draw_card(10)
