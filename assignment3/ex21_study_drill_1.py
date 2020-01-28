def make_phrase(input):
    phrase = "This is your text: {}".format(input)
    return phrase

print("Enter some input.")
print(make_phrase(input()))

def make_phrase2(input):
    phrase = f"This is your text: {input}"
    return phrase

print("Enter some input.")
print(make_phrase2(input()))
