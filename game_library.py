import time as t
import random
global playing
global player_turn
suits = ('Hearts','Diamonds','spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
val ={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10 ,'Queen':10, 'King':10, 'Ace':11}
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank +' of '+ self.suit
#card = Card(suits,ranks)
class Deck():
    def __init__(self,suits,ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        show_list=''
        for i in self.deck:
            show_list+=i.__str__()+"\n"
        return show_list
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return random.choice(self.deck)
    def __len__(self):
        lens = len(self.deck)
        print(f'the deck has {lens} cards')
#mydeck=Deck(suits,ranks)
#print(mydeck)
class Hand():
    def __init__(self):
        self.card=[]
        self.values=0
        self.aces=0
    def add_card(self,cards):
        self.card.append(cards)
        self.values+=val[cards.rank]
        if cards.rank=="Ace":
            self.aces+=1
    def add_values(self,cards):
        self.values+=val[cards.rank]
    def adjust_ace(self):
        if self.values > 21 and self.aces:
            self.values-=10
        else:
            self.aces-=1
player_card = Card(suits,ranks)
player_hand = Hand()
#player_hand.add_card(player_card.rank)
class Chips():
    def __init__(self):
        self.total=100
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
def take_bet(chip):
    while True:
        try:
            chip.bet=int(input("How much chips do u want to bet : "))
        except:
            print("Please enter only integer..")
        else:
            if chip.bet> chip.total:
                print("your bet amount cant exceed ur total")
            else:
                break
def hit(deck,hand):
    hits=deck.deal()
    hand.card.append(hits)
    hand.add_values()
def hit_or_stand(deck,hand):
    while True:
        choice1=input("hit or stand ? please write 's' or 'h':")
        if choice1 == "h":
            hit(deck,hand)
            return True
        elif choice1 == "s":
            print("Player choose stand")
            return False
        else:
            print("Invalid keywords")
            continue
        break
def show_value(player,dealer):
    print("The dealer first card is hidden!")
    print("the dealer second card :",dealer.card[0])
    print("the players cards are :")
    for i in player.card:
        print(i)
def show_all(player,dealer):
    print("The player cards and values are :")
    for i in player.card:
        print(i)
    print(player.total)
    print("The dealer cards and values are :")
    for i in dealer.card:
        print(i)
    print(dealer.total)
def win_check(player_chip,player_hand,dealer_hand):
    if player_hand.value < 21 and dealer_hand < player_hand:
        print("Player has won the game")
        player_chip.win_bet()
    elif player_hand.value < 21 and dealer_hand.value > player_hand.value:
        print("dealer has won the game")
        player_chip.lose_bet()
    else:
        print("the game was drawl")
        print("Nobody win")
def burst_check(player_hand,player_chip):
    if player_hand.values>21:
        print("Player burst")
        player_chip.lose_bet()
        playing= False
        player_turn=False
    else:
        playing=True
def computer_action(dealer_hand, deck):
        while True:
            try:
                ran = random.randint(1,0)
        #        choice1 = input("hit or stand ? please write 's' or 'h':")
                while dealer_hand.values<17:
                    if ran == 1:
                        hit(deck, dealer_hand)
                    elif ran == 0:
                        print("dealer choose to stand")
                        break
                    else:
                        continue
            except:
                print("your logic is not working")
            break
if __name__=="__main__":
    player_chip = Chips()
    take_bet(player_chip)
    print(player_chip.bet)
    dealer_hand=Hand()
    player_hand=Hand()
    computer_action(dealer_hand,deck=Deck(suits,ranks))
else:
    print("backend framework is imported")













