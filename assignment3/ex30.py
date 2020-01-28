people = 5
cars = 30
trucks = 45

# If mostly cars then take them
if cars > people or trucks < cars:
    print("We should take the cars.")
    # If more ppl than cars then don't
elif cars < people:
    print("We should not take the cars.")
    # Other conditions...don't decide
else:
    print("We can't decide.")

# If mostly trucks, then it's too many
if trucks > cars and trucks > people:
    print("That's too many trucks.")
    # More cars = take the cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
    # Other conditions...don't decide
else:
    print("We still can't decide.")

# If cars are the minority, then take the trucks
if people > trucks or trucks > cars:
    print("Alright, let's just take the trucks.")
    # Otherwise stay home
else: print("Fine, let's stay home then.")
