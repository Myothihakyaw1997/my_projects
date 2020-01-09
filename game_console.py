from game_library import*
import time
game_on=True
computer_turn=False
player_turn=True
while game_on:
    print("welcome to the black jack game")
    player_hand=Hand()
    dealer_hand=Hand()
    player_chip=Chips()
    player_card=Card(suits,ranks)
    dealer_card=Card(suits,ranks)
    deck=Deck(suits,ranks)
    deck.shuffle()
    playing = True
    while playing:
        player_hand.add_card(player_card)
        player_hand.add_card(player_card)
        dealer_hand.add_card(dealer_card)
        dealer_hand.add_card(dealer_card)
        deck.shuffle()
        print("Now the cards are shuffling!!")
        time.sleep(2)
        while player_turn:
            show_value(player_hand,dealer_hand)
            time.sleep(1)
            val=hit_or_stand(deck,player_hand)
            if val == True:
                print("Player chose hit,player_card is now increased!")
                player_hand.add_values()
            elif val == False:
                playing=False
                player_turn=False
            time.sleep(1)
            #burst_check(player_hand,player_chip)
            #if player_hand:
        playing=False
        computer_turn=True
    while computer_turn:
        if player_hand.values<=21:
            while dealer_hand.values < 17:
                hit(deck,dealer_hand)
                if dealer_hand.values >21:
                    print("Player has won")
                    player_chip.win_bet()
                    break
                else:
                    continue
            show_all(player_hand,dealer_hand)
            win_check(player_chip,player_hand,dealer_hand)
            playing=False
    ans=input("do you want to replay the game , y/n :")
    if ans[0].lower()=="y":
        game_on=True
    elif ans[0].lower()=='n':
        game_on=False
        print("Thanks you for playing the game")



