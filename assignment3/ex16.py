# Load argv from sys package
from sys import argv

# Expect script and filename inputs
script, filename = argv

# Empty threat to erase whatever file we mention
print(f"We're going to erase {filename}")
# Fake choices
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Request input, don't save it
input("?")

print("Opening the file...")
# Open the filename provided at start
target = open(filename, "w")
print("Truncating the file. Goodbye!")
# Empty the file
# target.truncate()

print("Now I'm going to ask you for three lines")

# Request input for three lines of text
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Write the three lines of text to the file that has been emptied.
target.write(f"{line1} \n {line2} \n {line3} \n")

# Close it upon finishing.
print("And finally, we close it.")
target.close()
