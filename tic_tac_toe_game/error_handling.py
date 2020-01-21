def ask():
    conn = True
    while conn:

        try:
            a = input("please write down any integer :")
            print(a ** 2)

        except:
            c = int(input("please write only integer like ' 1,12,30,33,56,1232,etc '"))
            print(c ** 2)
            print("unbelievable !!! how the hell did u do that ! u are super genius")
            conn = False

        else:
            print("You are amazing , super man dude, super man ")

ask()

