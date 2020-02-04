from sys import exit

def loading_screen():
    print("Welcome, traveler. Please tell me your name")

    traveler_name = input("< ")

    print(f"Ah, thank you, {traveler_name}. Are you prepared to face your destiny?")

    destiny = input("< ")

    # Two ways to skin a cat:
    # if (destiny == "no" or destiny == "No"):
    if (("no" in destiny) or ("No" in destiny)):
        print("Come back when you have thought this through.")
    elif (destiny == "yes" or destiny == "Yes"):
        print("In what town do you want to live: Carlin, Thais, or Venore?")
        town = input("< ")

        profession_text = vocation_screen(town)

        if "Knight" in profession_text:
            profession_choice = "knight"
            print("A KNIGHT! Are you sure? This decision is irreversible!")
        elif "Paladin" in profession_text:
            profession_choice = "paladin"
            print("A PALADIN! Are you sure? This decision is irreversible!")
        elif "Sorcerer" in profession_text:
            profession_choice = "sorcerer"
            print("A SORCERER! Are you sure? This decision is irreversible!")
        elif "Druid" in profession_text:
            profession_choice = "druid"
            print("A DRUID! Are you sure? This decision is irreversible!")
        else:
            print("...")
            print("I'm a pedant; please use proper spelling and capitalization.")
            vocation_screen(town)

        you_sure = input("< ")

        if "yes" or "Yes" in you_sure:
            print("So be it!")
        else:
            print("Come back when you have thought this through.")
    else:
        print("What?")


def vocation_screen(town):
    print(f"In {town}! And what profession have you chosen: Knight, Paladin, Sorcerer, or Druid?")

    profession_response = input("< ")

    return profession_response

loading_screen()
