import math as m

name = input("What is your name :")
print(f"Hello {name} ")
lenName = len(name)
print("the length of ur name is {}".format(lenName))
if lenName > 10:
    print("u have a very long name")
else:
    pass
if 'myo' in name:
    print("Ohh my god ! u are the genius")
a = input(" Do u want to solve pythagora problem ? : yes or no")
if a[0] == "y":
    d = int(input("please choose the values of x :"))
    f = int(input("please choose the values of y :"))
def pythagoras(x,y):
    z = m.sqrt(x**2 + y **2)
    return z
answ = pythagoras(d,f)
print(" the answer is {}".format(int(answ)))
def triangle_3rd_degree(d1 , d2 ):
    return (180 - (d1 + d2))
print(triangle_3rd_degree(20,30))


