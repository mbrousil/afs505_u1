# Create a mapping of counties to abbreviations
counties = {
  "Asotin": "AS",
  "Whitman": "WT",
  "Garfield": "GA",
  "Columbia": "CU"
}

# Create a basic set of counties and some cities in them
cities = {
  "WT": "Pullman",
  "GA": "Pomeroy",
  "CU": "Dayton"
}

# Add some more cities
cities["AS"] = "Clarkston"

# Print out some cities
print("-" * 10)
print("Asotin has: ", cities["AS"])
print("Whitman has: ", cities["WT"])

# Print some counties
print("-" * 10)
print("Whitman's abbreviation is: ", counties["Whitman"])
print("Garfield's abbreviation is: ", counties["Garfield"])

# Do it by using the county then cities dict
print("-" * 10)
print("Whitman has: ", cities[counties["Whitman"]])
print("Columbia has: ", cities[counties["Columbia"]])

# Print every state abbreviation
print("-" * 10)
for county, abbrev in list(counties.items()):
    print(f"{county} is abbreviated {abbrev}")

# Print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Now do both at the same time
print("-" * 10)
for county, abbrev in list(counties.items()):
    print(f"{county} county is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print("Now, for some other stuff:")

# Dictionaries as lists
print(list(counties))
print(list(cities))

# A loop over two dictionaries simultaneously
for a, b in zip(counties, cities):
    print(f"{a} contains {b}")

# Dictionary wants something named 1 I believe, not index 1:
print(counties[1])
