print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
        print("There's a treasure chest. What do you do?")
        print("1. Open it.")
        print("2. Test it for traps.")

        action = input("> ")

        if action == "1":
            print("It opens a pit in the floor and you fall into an extradimensional void.")
            print("Forever.")
        elif action == "2":
            print("You detect a trap, disarm it, and loot a trillion gold.")
            print("Nice.")
        else:
            print("Didn't consider that option, but let's say it didn't work out.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall ona knife and die. Good job!")
