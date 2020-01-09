import random as ran
from game_library import *
suits = ('Hearts','Diamonds','spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values ={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10 ,'Queen':10, 'King':10, 'Ace':11}
print("Welcome to blackjack game")
name = input("What is your name : ")
player_deck = Deck(suits,ranks)
card = Card(suits,ranks)
dealer_deck = Deck(suits,ranks)
#dealer_card = Card()
player_hand = Hand()
dealer_hand = Hand()
player_chips = Chips()
take_bet(player_chips)
player_turn = True
dealer_turn = False
player_hand.add_card(card)
player_hand.add_card(card)
dealer_hand.add_card(card)
dealer_hand.add_card(card)
count=0
while playing:
    while player_turn:
        show_value(player_hand, dealer_hand)
        con1=hit_or_stand()
        if not con1:
            player_turn = False
            dealer_turn = True
        burst=burst_check(player_hand,player_chip=player_chips)
        if burst:
            player_turn = False
            dealer_turn = False
        choice = input("")

    while dealer_turn:
        show_value(player_hand, dealer_hand)
        con2 = computer_action()
        if not con2:
            player_turn= True
            dealer_turn=False
        burst=burst_check()
        if burst:
            player_turn = False
            dealer_turn = False
    win = win_check(player_chip=player_chips, player_hand=player_hand, dealer_hand=dealer_hand)
    if win:
        playing=False




