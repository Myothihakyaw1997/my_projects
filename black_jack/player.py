class Player:
    def __init__(self , name  , age , gender , skill):
        self.name = name
        self.age = age
        self.gender = gender
        self.skill = skill
        self.bal = 1000
    def bet(self,amount):
        reduce_bal =  self.bal - amount
        self.bal = self.bal - reduce_bal
        return "remaing bal is {}".format(self.bal)
    def __str__(self):
        print("this is a player class")
    def __len__(self):
        print("the length function cant be used on player object")
    def stay(self):
        pass
class myo(Player):
    def puch(self , force):
        print(f"Puch with : {force}")
    def laugh(self):
        print(" Hahaha !!")
if __name__=="__main__":
    print("player module is runned")
else:
    print("Player module is imported")
