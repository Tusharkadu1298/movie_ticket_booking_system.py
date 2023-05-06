while True:
    print("*"*50)
    print("welcome to movie cinema")
    print("*"*50)
    print('''
    press 1 to watch fast x
    press 2 to watch the super mario
    press 3 to watch evil dead war
    press 4 to watch john wick
    ''')
    c = int(input("choose which movie you want to watch :-- "))
    if c == 1 :
        print("you have selcted fast x")
    elif c == 2:
        print("you have selected to watch super mario")
    elif c == 3:
        print("you have selected to watch evil dead war")
    elif c == 4 :
        print("you have selected to watch john wick") 
    print('''
    press 1 for basic
    press 2 for balcony
    press 3 for recliner  
    ''')
    choice = int(input("select which seat you want:-- "))
    print('''
    basic seat are 150
    balcony seat are 120
    recliners seat are 20 
    ''')
    basic = 150
    balcony = 120
    recliner = 50
    seat = int(input("how much seat do you want :-- "))
    if choice == 1:
        amount = 200*seat
        print(amount)
    elif choice == 2:
        amount1 = 300*seat
        print(amount1)
    elif choice == 3:
        amount2 = 500*seat
        print(amount2)
    else:
        print(" invalid please try again")
        print("these much seat are left")
    combo = input("do you want to add combo pack for rs 100/- ")
    if combo == "yes":
        b = int(input("how much combo you want :- "))
        camount = 100*b
        print("combo meal",camount)
    else:
        print("-"*40)
        print("ok")
        print("-"*40)
    if choice == 1 and combo == "yes":
        print("-"*40)
        print("your total price",amount + camount )
    elif choice == 2 and combo == "yes":
        print("-"*40)
        print("your total price",amount1 + camount )
    elif choice == 3 and combo == "yes":
        print("-"*40)
        print("your total price",amount2 + camount)
    print("enjoy your movie")
    print("-"*40)
    repeat1 = input("go to next person ? ")
    if repeat1 == "no":
        break
