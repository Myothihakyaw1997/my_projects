import random
card_value = [i for i in range(1,14)]
limit = 21
cards = ['1','2','3''4','5','6','7','8','9','jack','king','queen','aces']
class Player:
    def __init__(self,value,bank =1000):
        self.value = value
        self.bank = bank
        self.ran = 0
    def bet(self,amount):
        self.bank-=amount
        return amount
    def stay(self):
        continue
    def hit(self):
        self.ran +=random.randint(1,14)
        return self.ran
    def burst(self):
        if ran > limit :
            return "Game Over"
class Computer(Player):
    def __ran__(self):
        action = random.randint(1,2)
        return action
player = Player()
computer = Computer
def win_check():
    if player.ran > computer.ran:
        print("player has won the game")
    if player.ran < computer.ran:
        print("Game over")
game_on = True
print("Welcome to Black Jack game")
while game_on:
    print("do you want to start")






