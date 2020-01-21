class Calculator():
    def __init__(self,power):
        self.process = "calculation"
        self.structure = "square shape "
        self.texture = "soft"
        self.color = "wide range of colour "
        self.ability = power
    def __str__(self):
        print("This is calculator")
    def __len__(self):
        return 100
    def add(self,a,b):
        self.answer = a + b
        print(self.answer)
        return self.answer
    def sub(self,a ,b):
        self.answer = abs(a-b)
        print(self.answer)
        return self.answer
    def mul(self,a,b):
        print(a*b)
        return a*b
    def div(self,a,b):
        print(a/b)
        return a/b

if __name__=="__main__":
    print("program 1 runned !")
else:
    print("program 1 imported !!")