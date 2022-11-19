print("Welcome To the Adventure Game\nThe Rules\nY-Yes\nN-No\nQ-Quit\nChoose Option 1 or Option 2.\n")
age = int(input("How old are you?"))

if age > 18:
    print(f"You are {age} years old so you old enough\n")
    Response = input("Do you wish to play?\nYes/No: ").lower()

    if Response == "y":
        print("Let's proceed\n")

        Dest_1 = input("Where would you like to go?\nOption 1: The movies\nOption 2: The shops\n").lower()


        if Dest_1 == "option 1":
            print("When you got to the movies you saw that it was shut.\n")
            Dest_1a = input("You decided to go to the\nOption 1: forest for a walk\nOption 2: beach for a swim\n").lower()
            if Dest_1a == "option 1":
                print("When you got to the forest, you went for a walk up the hill.\n")
                Dest_1b = input(" Once you finished walking it was time to go home. But first you went to get a\nOption 1: milkshake\nOption 2: smoothie\n").lower()
                if Dest_1b == "option 1":
                    print("You got poisoned and died oof\n")
                else:
                    print("You got an uncurable disease from the smoothie\n")


            elif Dest_1a == "option 2":
                print("When we got to the beach we went for a swim on our boogie boards.\n")
                Dest_1ab = input(" It was so cold so you had:\nOption 1: get a Starbucks coffee\nOption 2: get a hot chocolate\n").lower()
                if Dest_1ab == "option 1":
                    print("You suffered from 3rd degree burn oof\n")
                else:
                    print("It was the best chocolate of your life\n")


        elif Dest_1 == "option 2":
            print("The shops were lots of fun\n")
            Dest_2a = input( "You got hungry so you decided to get food at\nOption 1: Mcdonalds\nOption 2: Mexican Restaurant\n").lower()
            if Dest_2a == "option 1":
                print("When you got to mcdonalds you had a big mac combo with a chocolate milkshake. It was so delicious")
                Dest_2b = input("My tummy was so full so afterwards we went for a:\nOption 1: walk along the waterfront\nOption 2:sit at the park\n").lower()
                if Dest_2b == "option 2":
                    print("you had the best time of your time\n")
                else:
                    print("A snake came out of nowhere and bit you. oof\n")


            elif Dest_2a == "option 2":
                print("I had a burrito for lunch.\n")
                Dest_2ab = input("we quickly visited the\nOption 1: park\nOption 2: playground").lower()
                if Dest_2ab == "option 2":
                    print("You met Ariana Grande\n")
                else:
                    print("You saw your crush\n")
    else:
        print("Fuck you")