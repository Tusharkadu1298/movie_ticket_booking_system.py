print("*"*40)
print("welcome to movie cinema")
print("*"*40)
name = input("enter your name :--")
print("welcome", name )
print('''
press 1 to watch fast x
press 2 to watch the super mario
press 3 to watch evil dead war
press 4 to watch john wick
  ''')
while True:
    c = int(input("choose which movie you want to watch :--"))
    if c == 1 :
        print("you have selcted fast x ")
    elif c == 2:
        print("you have selected to watch super mario ")
    elif c == 3:
        print("you have selected to watch evil dead war" )
    elif c == 4 :
        print("you have selected to watch john wick" ) 
    else:
        print("invalid number,try again")
    if c == 1 :
        while True:
            print('''
            press 1 for normal rs - 200
            press 2 for balcony rs - 300
            press 3 for recliner  - 500 
            ''')
            print('''
            normal seats are 150
            balcony seat are 150
            recliners seat are 50
            '''
            )
            normal= 150
            balcony = 150
            recliners = 50
            choice = int(input("select which seat you want:-- "))
            seat = int(input("how much seat do you want :-- "))
            if choice == 1:
                if seat > normal:
                    print("housefull")
                else:
                    normal -= seat
                    print("these much seat are left :--",normal)
                    amount = 200*seat
                    print(amount)
            elif choice == 2:
                if seat > balcony:
                    print("housefull")
                else:
                    balcony -= seat
                    print("these much seat are left :--",balcony)
                    amount1 = 300*seat
                    print(amount1)
            elif choice == 3:
                if seat > recliners:
                    print("housefull")
                else:
                    recliners -= seat
                    print("these much seat are left :--",recliners)
                    amount2 = 500*seat
                    print(amount2)
            else:
                print(" invalid please try again")
            
            repeat = input("do you want to add more tickets ? ")
            if repeat == "no":
                break
        combo = input("do you want to add combo pack for rs 100/- ")
        if combo == "yes":
            b = int(input("how much combo you want :- "))
            camount = 100*b
            print("combo meal",camount)
        else:
            print("ok")
        if choice == 1 and combo == "no":
            print("-"*40)
            print("your total price",amount)
        elif choice == 2 and combo == "no":
            print("-"*40)
            print("your total price",amount1)
        elif choice == 3 and combo == "no":
            print("-"*40)
            print("your total price",amount2)
        print("ejoy your movie")
        print("-"*40)
        if choice == 1 and combo == "yes":
            print("-"*40)
            print("your total price",amount + camount )
            print("-"*40)
        elif choice == 2 and combo == "yes":
            print("-"*40)
            print("your total price",amount1 + camount )
            print("-"*40)
        elif choice == 3 and combo == "yes":
            print("-"*40)
            print("your total price",amount2 + camount)
            print("-"*40)
        break
    if c == 2:
        while True:
            print('''
            press 1 for normal rs - 250
            press 2 for balcony rs - 350
            press 3 for recliner  - 500 
            ''')
            print('''
            normal seats are 110
            balcony seat are 140
            recliners seat are 20
            '''
            )
            normal= 250
            balcony = 350
            recliners = 20
            choice = int(input("select which seat you want:-- "))
            seat = int(input("how much seat do you want :-- "))
            if choice == 1:
                if seat > normal:
                    print("housefull")
                else:
                    normal -= seat
                    print("these much seat are left :--",normal)
                    amount = 250*seat
                    print(amount)
            elif choice == 2:
                if seat > balcony:
                    print("housefull")
                else:
                    balcony -= seat
                    print("these much seat are left :--",balcony)
                    amount1 = 350*seat
                    print(amount1)
            elif choice == 3:
                if seat > recliners:
                    print("housefull")
                else:
                    recliners -= seat
                    print("these much seat are left :--",recliners)
                    amount2 = 500*seat
                    print(amount2)
            else:
                print(" invalid please try again")
            
            repeat = input("do you want to add more tickets ? ")
            if repeat == "no":
                break
        combo = input("do you want to add combo pack for rs 100/- ")
        if combo == "yes":
            b = int(input("how much combo you want :- "))
            camount = 100*b
            print("combo meal",camount)
        else:
            print("ok")
        if choice == 1 and combo == "no":
            print("-"*40)
            print("your total price",amount)
        elif choice == 2 and combo == "no":
            print("-"*40)
            print("your total price",amount1)
        elif choice == 3 and combo == "no":
            print("-"*40)
            print("your total price",amount2)
        print("ejoy your movie")
        print("-"*40)
        if choice == 1 and combo == "yes":
            print("-"*40)
            print("your total price",amount + camount )
            print("-"*40)
        elif choice == 2 and combo == "yes":
            print("-"*40)
            print("your total price",amount1 + camount )
            print("-"*40)
        elif choice == 3 and combo == "yes":
            print("-"*40)
            print("your total price",amount2 + camount)
            print("-"*40)
        break
    if c == 3:
        while True:
            print('''
            press 1 for normal rs - 200
            press 2 for balcony rs - 300
            press 3 for recliner  - 500 
            ''')
            print('''
            normal seats are 150
            balcony seat are 150
            recliners seat are 50
            '''
            )
            normal= 150
            balcony = 150
            recliners = 50
            choice = int(input("select which seat you want:-- "))
            seat = int(input("how much seat do you want :-- "))
            if choice == 1:
                if seat > normal:
                    print("housefull")
                else:
                    normal -= seat
                    print("these much seat are left :--",normal)
                    amount = 200*seat
                    print(amount)
            elif choice == 2:
                if seat > balcony:
                    print("housefull")
                else:
                    balcony -= seat
                    print("these much seat are left :--",balcony)
                    amount1 = 300*seat
                    print(amount1)
            elif choice == 3:
                if seat > recliners:
                    print("housefull")
                else:
                    recliners -= seat
                    print("these much seat are left :--",recliners)
                    amount2 = 500*seat
                    print(amount2)
            else:
                print(" invalid please try again")
            
            repeat = input("do you want to add more tickets ? ")
            if repeat == "no":
                break
        combo = input("do you want to add combo pack for rs 100/- ")
        if combo == "yes":
            b = int(input("how much combo you want :- "))
            camount = 100*b
            print("combo meal",camount)
        else:
            print("ok")
        if choice == 1 and combo == "no":
            print("-"*40)
            print("your total price",amount)
        elif choice == 2 and combo == "no":
            print("-"*40)
            print("your total price",amount1)
        elif choice == 3 and combo == "no":
            print("-"*40)
            print("your total price",amount2)
        print("ejoy your movie")
        print("-"*40)
        if choice == 1 and combo == "yes":
            print("-"*40)
            print("your total price",amount + camount )
            print("-"*40)
        elif choice == 2 and combo == "yes":
            print("-"*40)
            print("your total price",amount1 + camount )
            print("-"*40)
        elif choice == 3 and combo == "yes":
            print("-"*40)
            print("your total price",amount2 + camount)
            print("-"*40)
        break
    if c == 4:
        while True:
            print('''
            press 1 for normal rs - 100
            press 2 for balcony rs - 250
            press 3 for recliner  - 350
            ''')
            print('''
            normal seats are 150
            balcony seat are 150
            recliners seat are 50
            '''
            )
            normal= 150
            balcony = 150
            recliners = 50
            choice = int(input("select which seat you want:-- "))
            seat = int(input("how much seat do you want :-- "))
            if choice == 1:
                if seat > normal:
                    print("housefull")
                else:
                    normal -= seat
                    print("these much seat are left :--",normal)
                    amount = 100*seat
                    print(amount)
            elif choice == 2:
                if seat > balcony:
                    print("housefull")
                else:
                    balcony -= seat
                    print("these much seat are left :--",balcony)
                    amount1 = 250*seat
                    print(amount1)
            elif choice == 3:
                if seat > recliners:
                    print("housefull")
                else:
                    recliners -= seat
                    print("these much seat are left :--",recliners)
                    amount2 = 350*seat
                    print(amount2)
            else:
                print(" invalid please try again")
            
            repeat = input("do you want to add more tickets ? ")
            if repeat == "no":
                break
        combo = input("do you want to add combo pack for rs 100/- ")
        if combo == "yes":
            b = int(input("how much combo you want :- "))
            camount = 100*b
            print("combo meal",camount)
        else:
            print("ok")
        if choice == 1 and combo == "no":
            print("-"*40)
            print("your total price",amount)
        elif choice == 2 and combo == "no":
            print("-"*40)
            print("your total price",amount1)
        elif choice == 3 and combo == "no":
            print("-"*40)
            print("your total price",amount2)
        print("ejoy your movie")
        print("-"*40)
        if choice == 1 and combo == "yes":
            print("-"*40)
            print("your total price",amount + camount )
            print("-"*40)
        elif choice == 2 and combo == "yes":
            print("-"*40)
            print("your total price",amount1 + camount )
            print("-"*40)
        elif choice == 3 and combo == "yes":
            print("-"*40)
            print("your total price",amount2 + camount)
            print("-"*40)
        break
