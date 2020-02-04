print("Hail and well met!")
print("What's your name, mortal?")

traveler_name = input("> ")

print(f"Ah, {traveler_name}. A fine title.")
print("""Are you:
1. a fighter, or
2. a mage?""")

vocation = input("< ")

if vocation == "1":
    print("A fighter eh? You should go lift some weights.")
    print("""1. Yes
    2. No""")

    workout = input("> ")

    if workout == "1":
        print("Great you get stronger!")
    elif workout == "2":
        print("Ah, you lose in a fight and die.")
    else:
        print("Woah you're the strongest in Letterkenny.")

elif vocation == "2":
    print("A mage? Sick. Go study your cantrips.")
    print("""1. Yes
    2. No""")

    study = input("> ")

    if study == "1":
        print("You become a crazy good wizard.")
    elif study == "2":
        print("A fighter beats you cuz you didn't learn cantrips. You're dead.")
    else:
        print("Woah, no one's tried that before. You are the best wizard ever.")
